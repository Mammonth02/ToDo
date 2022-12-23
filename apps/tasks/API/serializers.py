from rest_framework import serializers

from ..models import Task

class TasksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'discription', 'date_time', 'image']

class TasksGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'date_time', 'done']

class SingleTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'discription', 'date_time', 'done', 'image']

class DeleteAllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = []