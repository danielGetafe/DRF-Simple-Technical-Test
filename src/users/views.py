from rest_framework.generics import CreateAPIView, RetrieveAPIView

from src.users.models import User
from src.users.serializers import UserSerializer

# Create your views here.


class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
