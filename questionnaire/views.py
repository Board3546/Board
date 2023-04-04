import json
from datetime import datetime, timedelta

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import transaction
from django.db.models import F
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
)

from questionnaire.forms import CreateServiceForm
from questionnaire.models import Service, Category, Review, Addition, OnTopPrice
from questionnaire.tasks import subscription_inactive
from questionnaire.utils import save_images, save_additions
from users.models import Profile


class ServicesListView(ListView):
    """Display all services"""

    model = Service
    template_name = "questionnaire/services_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.filter(is_published=True).prefetch_related("images")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["additions"] = Addition.objects.filter(price=0)
        return context


class ServiceView(DetailView):
    """Display service by slug"""

    model = Service
    template_name = "questionnaire/service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additions"] = (
            context.get("service").additions.all().select_related("category")
        )
        context["reviews"] = Review.objects.filter(
            service=context.get("service"), moderated=True
        )
        context["images"] = context.get("service").images.filter(moderated=True)
        context["main_image"] = context.get("service").images.filter(moderated=True)[0]
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        return Service.objects.all().prefetch_related("images", "reviews")


class FavoritesView(View):
    def get(self, request):
        try:
            stores = json.loads(self.request.COOKIES.get("key")).get("stores")
        except TypeError:
            stores = []
        services_ids = (int(x) for x in stores)
        services = Service.objects.filter(pk__in=services_ids)
        return render(
            request=request,
            template_name="questionnaire/favorites.html",
            context={"services": services},
        )


class PostServiceReviewView(View):
    def post(self, request, pk):
        try:
            original_photo = True if "original_photo" in self.request.POST else None
            service = Service.objects.get(pk=pk)
            Review.objects.create(
                user=self.request.POST.get("user"),
                message=self.request.POST.get("message"),
                original_photo=original_photo,
                service=service,
                stars=5,
            )
            return JsonResponse(
                data={"ok_message": "Ваш отзыв отправлен на модерацию."}, status=201
            )
        except (MultipleObjectsReturned, ObjectDoesNotExist):
            return JsonResponse(
                data={
                    "error": "Что-то пошло не так, повторите попытку позже. Если ошибка не исчезнет, напишите нам"
                },
                status=400,
            )


class SubscriptionPaymentView(View):
    @transaction.atomic
    def post(self, request, pk):
        """Decries user balance and make service active by current pk"""
        profile = Profile.objects.get(user=self.request.user)
        service = Service.objects.get(pk=pk)
        if profile.balance >= service.type:
            profile.balance = F("balance") - service.type
            profile.save()
        else:
            raise AttributeError("Недостаточно денег на балансе")

        service.subscription_expire = datetime.utcnow() + timedelta(days=30)
        service.subscription_active = True
        service.save(update_fields=["subscription_expire", "subscription_active"])
        subscription_inactive.apply_async(
            (pk,), eta=datetime.utcnow() + timedelta(days=30)
        )
        return redirect("payment-done", pk, permanent=True)


class SubscriptionPaymentDoneView(TemplateView):
    """Display payment done template"""

    template_name = "questionnaire/payment_done.html"


class CreateServiceView(CreateView):
    """Create service using model form"""

    form_class = CreateServiceForm
    template_name = "questionnaire/service_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_additions"] = Addition.objects.filter(price=0)
        return context

    def form_valid(self, form):
        object = form.save()
        save_images(self.request, object)
        save_additions(self.request, object)
        return HttpResponseRedirect(object.get_absolute_url())


class FilterView(View):
    def get(self, request, *args, **kwargs):
        filter_params = {
            filter_param: (
                value == "True" if value == "True" or value == "False" else value
            )
            for filter_param, value in self.request.GET.items()
        }
        services = Service.objects.filter(
            is_published=True, **filter_params
        ).prefetch_related("images")
        return render(
            request,
            "questionnaire/services_list.html",
            {"services": services, "additions": Addition.objects.filter(price=0)},
        )


class VideoView(ListView):
    model = Service
    template_name = "questionnaire/services_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.filter(
            is_published=True, subscription_active=True
        ).exclude(video="")


class TransView(ListView):
    model = Service
    template_name = "questionnaire/services_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.filter(
            is_published=True, subscription_active=True
        ).exclude(gender="Натуралка/Натурал")


class ReviewsView(ListView):
    model = Review
    template_name = "questionnaire/services_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return Review.objects.filter(moderated=True).select_related("service")


class NewServicesView(ListView):
    model = Service
    template_name = "questionnaire/services_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.filter(
            is_published=True, subscription_active=True
        ).order_by("-date_published")


class RiseOnTopServiceView(View):
    @transaction.atomic
    def post(self, request, pk):
        """Rise current service on top of its subscription level"""
        current_price = OnTopPrice.objects.get(pk=1).price
        profile = Profile.objects.get(user=self.request.user)
        service = Service.objects.get(pk=pk)
        if profile.balance >= current_price:
            profile.balance = F("balance") - current_price
            profile.save()
        else:
            raise AttributeError("Недостаточно денег на балансе")

        service.on_top = datetime.utcnow()
        service.save(update_fields=["on_top"])
        return redirect("ontop-done", pk, permanent=True)


class OnTopDoneView(TemplateView):
    template_name = "questionnaire/ontop_done.html"


class UpdateServiceView(UpdateView):
    """Update service using model form"""

    form_class = CreateServiceForm
    template_name = "questionnaire/service_update.html"
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_additions"] = Addition.objects.filter(price=0)
        return context

    def form_valid(self, form):
        object = form.save()
        save_images(self.request, object)
        save_additions(self.request, object)
        return HttpResponseRedirect(object.get_absolute_url())


class PublishOrUnpublishView(View):
    def post(self, request):
        try:
            service = Service.objects.get(id=self.request.POST.get("service_id"))
            service.is_published = int(self.request.POST.get("flag"))
            service.save()
            return JsonResponse(
                data={"ok_message": "Показ анкеты изменен, обновите страницу."},
                status=201,
            )
        except (MultipleObjectsReturned, ObjectDoesNotExist):
            return JsonResponse(
                data={
                    "error": "Что-то пошло не так, повторите попытку позже. Если ошибка не исчезнет, напишите нам"
                },
                status=400,
            )
