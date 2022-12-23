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

