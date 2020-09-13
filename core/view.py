from rest_framework import generics, permissions
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """ Creating new regular user"""

    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny,)
