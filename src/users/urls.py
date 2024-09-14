from django.urls import path

from src.users.views import RegisterUserAPIView, UserAPIView

urlpatterns = [
    path("users/register", RegisterUserAPIView.as_view(), name="register-user"),
    path("users/<int:pk>", UserAPIView.as_view(), name="user-profile"),
]
