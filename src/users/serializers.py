from rest_framework import serializers

from src.users.tasks import task_validate_account
from src.users.models import User
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
            task_validate_account.delay(
                email_address=created_user.email,
                first_name=created_user.first_name,
                phone_number=created_user.phone_number,
            )
        return created_user
