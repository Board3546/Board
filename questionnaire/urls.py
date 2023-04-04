from django.urls import path

from questionnaire.views import (
    ServicesListView,
    ServiceView,
    FavoritesView,
    PostServiceReviewView,
    SubscriptionPaymentView,
    SubscriptionPaymentDoneView,
    CreateServiceView,
    FilterView,
    VideoView,
    RiseOnTopServiceView,
    OnTopDoneView,
    UpdateServiceView,
    PublishOrUnpublishView,
    TransView, ReviewsView, NewServicesView,
)

urlpatterns = [
    path("", ServicesListView.as_view(), name="home"),
    path("favorites/", FavoritesView.as_view(), name="favorites"),
    path("<int:pk>/", ServiceView.as_view(), name="service"),
    path("<int:pk>/review/", PostServiceReviewView.as_view(), name="review"),
    path(
        "service/publish-or-unpublish/",
        PublishOrUnpublishView.as_view(),
        name="publish-or-unpublish",
    ),
    path("service/create/", CreateServiceView.as_view(), name="create-service"),
    path(
        "service/update/<int:pk>/", UpdateServiceView.as_view(), name="update-service"
    ),
    path("<int:pk>/pay/", SubscriptionPaymentView.as_view(), name="pay"),
    path("on-top/<int:pk>/", RiseOnTopServiceView.as_view(), name="on-top"),
    path("services/filter/", FilterView.as_view(), name="services-filter"),
    path("services/video/", VideoView.as_view(), name="services-video"),
    path("services/trans/", TransView.as_view(), name="services-trans"),
    path("services/reviews/", ReviewsView.as_view(), name="services-reviews"),
    path("services/new/", NewServicesView.as_view(), name="services-new"),
    path(
        "<int:pk>/payment/done/",
        SubscriptionPaymentDoneView.as_view(),
        name="payment-done",
    ),
    path("<int:pk>/on-top/done/", OnTopDoneView.as_view(), name="ontop-done"),
]
