from enum import Enum

from datetime import timedelta, datetime

from django.utils import timezone
from django.core.validators import \
    validate_email, \
    RegexValidator


phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. "
    "Up to 15 digits allowed.",
)


def expire_at() -> datetime:
    from .conf import conf

    now = timezone.now()
    due_at = now + timedelta(seconds=conf.LIFETIME)

    return due_at


def send_code(func):
    """
    Try to get transport and send code

    """
    def wrapper(*args, **kwargs):
        from .tasks import otp_transport_handler

        result = func(*args, **kwargs)
        otp_transport_handler.delay(result.pk)

        return result

    return wrapper


class BaseTransport:
    def __init__(self, otp):
        self.otp = otp

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.otp = None

    def send_code(self):
        raise NotImplemented


class Transport(Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"

    def validator(self, value):
        if self == Transport.EMAIL:
            return validate_email(value)

        if self == Transport.SMS:
            return phone_regex(value)


