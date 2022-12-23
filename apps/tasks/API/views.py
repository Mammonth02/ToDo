from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from ..models import Task
from .serializers import TasksCreateSerializer, TasksGetSerializer, SingleTaskSerializer, DeleteAllTasksSerializer
from .permissions import IsOwner
from .service import TaskFilter

class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksCreateSerializer
    permission_classes = (IsOwner, )

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = TaskFilter
    search_fields = ['title']
    ordering_fields = ['create_time', 'date_time']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TasksGetSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TasksGetSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        tasks = Task.objects.filter(owner = self.request.user)
        return tasks

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return redirect('tasks')

class SingleTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = SingleTaskSerializer
    permission_classes = (IsOwner, )

class DeleteAllTasks(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = DeleteAllTasksSerializer
    permission_classes = (IsOwner, )

    def post(self, request, *args, **kwargs):
        Task.objects.filter(owner = self.request.user).delete()
        return redirect('tasks')