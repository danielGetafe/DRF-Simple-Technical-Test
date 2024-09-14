from django.core.mail import send_mail


def send_email_validate_user(email_address: str, first_name: str) -> None:
    send_mail(
        "Account created",
        f"Welcome {first_name}, your account has been created",
        "from@example.com",
        [email_address],
    )


def send_sms_validate_user(phone_number: str, first_name: str) -> None:
    pass
