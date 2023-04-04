from django.urls import path

from support import views

urlpatterns = [
    path("", views.SupportView.as_view(), name="support-main"),
    path("topic/<slug:slug>/", views.TopicView.as_view(), name="topic"),
    path("ticket/<slug:slug>/", views.TicketView.as_view(), name="ticket"),
    path(
        "my-tickets/<int:id>/",
        views.MyTicketsView.as_view(),
        name="support-my-tickets",
    ),
    path(
        "create-ticket/", views.CreateTicketView.as_view(), name="support-create-ticket"
    ),
    path("donation/", views.DonationView.as_view(), name="donation"),
    path("donation/done/", views.DonationDoneView.as_view(), name="donation-done"),
]
