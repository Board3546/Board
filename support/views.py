from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from support.filters import SupportTopicsFilter
from support.forms import CreateTicketForm, CreateSiteReviewForm
from support.models import Support, Ticket


# Create your views here.
class SupportView(ListView):
    model = Support
    template_name = "support/support_main.html"
    context_object_name = "topics"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        topics_filter = SupportTopicsFilter(self.request.GET, queryset)
        paginated_filtered_topics = Paginator(topics_filter.qs, 3)
        page_number = self.request.GET.get("page")
        if page_number is None:
            page_number = 1
        page_range = paginated_filtered_topics.get_elided_page_range(
            number=page_number, on_each_side=2, on_ends=1
        )
        topic_page_obj = paginated_filtered_topics.get_page(page_number)
        context["topic_page_obj"] = topic_page_obj
        context["filter"] = topics_filter
        context["page_range"] = page_range
        context["amount_of_pages"] = paginated_filtered_topics.num_pages
        return context


class TopicView(DetailView):
    model = Support
    template_name = "support/topic.html"
    context_object_name = "topic"


class TicketView(DetailView):
    model = Ticket
    template_name = "support/ticket.html"
    context_object_name = "ticket"


class MyTicketsView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = "support/my_tickets.html"
    context_object_name = "my_tickets"
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get("id") != self.request.user.id:
            raise PermissionDenied
        queryset = self.get_queryset()
        tickets = Paginator(queryset, 10)
        page_number = self.request.GET.get("page")
        if page_number is None:
            page_number = 1
        page_range = tickets.get_elided_page_range(
            number=page_number, on_each_side=2, on_ends=1
        )
        ticket_page_obj = tickets.get_page(page_number)
        context["ticket_page_obj"] = ticket_page_obj
        context["page_range"] = page_range
        context["amount_of_pages"] = tickets.num_pages
        return context

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user).select_related("user")


class CreateTicketView(LoginRequiredMixin, CreateView):
    form_class = CreateTicketForm
    template_name = "support/create_ticket.html"
    raise_exception = True


class DonationView(CreateView):
    form_class = CreateSiteReviewForm
    template_name = "donation.html"
    success_url = reverse_lazy("donation-done")


class DonationDoneView(TemplateView):
    template_name = "donation_done.html"
