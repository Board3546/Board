from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from users.forms import RegistrationForm
from users.models import Profile
from users.utils import services_count


class ProfileView(DetailView):
    """Preview user profile"""

    model = Profile
    template_name = "users/base_profile.html"

    def get_queryset(self):
        return Profile.objects.all().select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = services_count(context)
        return context


class RegisterUser(CreateView):
    """Register user by custom form"""

    form_class = RegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Login user after registration and create his profile"""
        user = form.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        login(self.request, user)
        return redirect("home")


class UserServicesGirlsView(DetailView):
    model = Profile
    template_name = "users/user_services_girls.html"

    def get_queryset(self):
        return Profile.objects.all().select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = services_count(context)
        return context


class UserServicesMassageView(DetailView):
    model = Profile
    template_name = "users/user_services_massage.html"

    def get_queryset(self):
        return Profile.objects.all().select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = services_count(context)
        return context


class UserServicesBoysView(DetailView):
    model = Profile
    template_name = "users/user_services_boys.html"

    def get_queryset(self):
        return Profile.objects.all().select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = services_count(context)
        return context


class UserServicesOrgsView(DetailView):
    model = Profile
    template_name = "users/user_services_orgs.html"

    def get_queryset(self):
        return Profile.objects.all().select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = services_count(context)
        return context
