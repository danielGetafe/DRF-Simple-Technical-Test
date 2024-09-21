from celery.utils.log import get_task_logger
from src.users.services import send_email_validate_user, send_sms_validate_user
from src.celery_app import celery_app

logger = get_task_logger(__name__)


@celery_app.task(bind=True)
def task_validate_account(
    self, email_address: str, first_name: str, phone_number: str
) -> None:
    logger("Starting task to validate user account with email: %s", email_address)
    send_email_validate_user(email_address, first_name)
    send_sms_validate_user(phone_number, first_name)
    logger("Finished task to validate user account with email: %s", email_address)
