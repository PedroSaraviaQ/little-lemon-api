from django.urls import path
from .views import index, BookingView, MenuView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index, name="index"),
    path("booking/", BookingView.as_view()),
    path("menu/", MenuView.as_view()),
    path("api-token-auth/", obtain_auth_token),
]
