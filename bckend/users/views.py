from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    API to register a new user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer