from django.urls import path

from .views import UserRegistrationAPI

urlpatterns = [
    path('user/', UserRegistrationAPI.as_view()),

]