from django.urls import path

from .views import UserRegistrationAPI, UserAPI

urlpatterns = [
    path('create/', UserRegistrationAPI.as_view()),
    path('<int:pk>/', UserAPI.as_view()),

]