from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from ..models import Task
from .serializers import TasksCreateSerializer, TasksGetSerializer
from .permissions import IsOwner

class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksCreateSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(owner = self.request.user)
        return Response(TasksGetSerializer(tasks, many=True).data)

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return redirect('tasks')