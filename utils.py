from datetime import \
    timedelta, \
    datetime

from django.utils import timezone


from .conf import conf


def expire_at() -> datetime:
    """
    End date when you may to use generated code

    """
    now = timezone.now()
    due_at = now + timedelta(seconds=conf.LIFETIME)

    return due_at


def send_code(func):
    def wrapper(*args, **kwargs):
        from .tasks import otp_transport_handler

        result = func(*args, **kwargs)
        otp_transport_handler.delay(result.pk)

        return result

    return wrapper
