from rest_framework import serializers

from src.users.models import User
from src.users.services import send_email_validate_user, send_sms_validate_user
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "hobbies",
            "is_email_verified",
            "is_phone_number_verified",
        ]
        read_only_fields = ["id", "is_email_verified", "is_phone_number_verified"]

    def create(self, validated_data):
        created_user = super().create(validated_data)
        if settings.SEND_VALIDATE_EMAIL_AND_SMS:
            send_email_validate_user(created_user.email, created_user.first_name)
            send_sms_validate_user(created_user.phone_number, created_user.first_name)
        return created_user
