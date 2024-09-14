from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField("First name", max_length=128)
    last_name = models.CharField("Last name", max_length=255)
    phone_number = models.CharField(
        "Phone number", max_length=32, unique=True
    )  # str in case of international prefix
    email = models.EmailField("Email", unique=True)

    hobbies = models.TextField("Hobbies", blank=True, null=True)

    is_email_verified = models.BooleanField("Is email verified", default=False)
    is_phone_number_verified = models.BooleanField(
        "Is phone number verified", default=False
    )

    def __str__(self):
        return f"{self.email}"
