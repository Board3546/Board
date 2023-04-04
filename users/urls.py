from django.urls import path
from django.views.generic import TemplateView

from users.views import (
    ProfileView,
    RegisterUser,
    UserServicesGirlsView,
    UserServicesMassageView,
    UserServicesBoysView,
    UserServicesOrgsView,
)

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("<int:pk>/", ProfileView.as_view(), name="profile"),
    path("<int:pk>/girls/", UserServicesGirlsView.as_view(), name="girls"),
    path("<int:pk>/massage/", UserServicesMassageView.as_view(), name="massage"),
    path("<int:pk>/boys/", UserServicesBoysView.as_view(), name="boys"),
    path("<int:pk>/orgs/", UserServicesOrgsView.as_view(), name="orgs"),
    path("balance/", TemplateView.as_view(template_name='users/top_up_balance.html'), name="balance"),
]
