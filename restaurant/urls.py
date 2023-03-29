from django.urls import path
from .views import index, BookingView, MenuView

urlpatterns = [
    path("", index, name="index"),
    path("booking/", BookingView.as_view()),
    path("menu/", MenuView.as_view()),
]
