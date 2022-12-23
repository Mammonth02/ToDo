from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..models import User
from .serializers import UserRegistrationSerializer, UserSerializer
from .permissions import IsUser

class UserRegistrationAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUser, )

class HomePage(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        else:
            return redirect('create_user')