from rest_framework import serializers

from ..models import Task

class TasksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'discription', 'date_time']

class TasksGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'date_time', 'done', 'owner']