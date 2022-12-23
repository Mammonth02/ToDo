from django.urls import path

from .views import Tasks, SingleTask, DeleteAllTasks

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('single/<int:pk>/', SingleTask.as_view(), name='single_tasks'),
    path('delete/all/', DeleteAllTasks.as_view(), name='delete_all'),

]