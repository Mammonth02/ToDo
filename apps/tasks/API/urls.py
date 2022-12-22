from django.urls import path

from .views import Tasks, SingleTask

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('single/<int:pk>/', SingleTask.as_view(), name='single_tasks'),

]