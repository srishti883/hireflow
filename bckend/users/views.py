from rest_framework import generics
from .models import User
from .serializers import UserSerializer



from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    API to register a new user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


# Profile API
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


