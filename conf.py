from enum import Enum

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.validators import \
    validate_email, \
    RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")


class TransportHandler:
    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def send(self, *args, **kwargs):
        raise NotImplemented


class SMSTransportHandler(TransportHandler):
    def send(self, *args, **kwargs):
        pass


class EmailTransportHandler(TransportHandler):
    def send(self, *args, **kwargs):
        pass


class Transport(Enum):
    SMS = 'sms'
    EMAIL = 'email'

    @classmethod
    def all(cls):
        return [e.value for e in Transport]

    def handler(self):
        pass

    def validator(self, value):
        if self == Transport.EMAIL:
            return validate_email(value)

        if self == Transport.SMS:
            return phone_regex(value)


OTP_PROVIDER = getattr(settings, "OTP_PROVIDER", {})
OTP_PROVIDER.setdefault("SIZE", 4)
OTP_PROVIDER.setdefault("ATTEMPTS", 3)
OTP_PROVIDER.setdefault("LIFETIME", 60)
OTP_PROVIDER.setdefault("TRANSPORT", Transport.EMAIL)
OTP_PROVIDER.setdefault("ERROR_TEXT", 'Please try again later')
OTP_PROVIDER.setdefault("CELERY", 'run_celery')


class Conf:
    SIZE = OTP_PROVIDER.get("SIZE")
    ATTEMPTS = OTP_PROVIDER.get("ATTEMPTS")
    LIFETIME = OTP_PROVIDER.get("LIFETIME")
    TRANSPORT = OTP_PROVIDER.get("TRANSPORT")
    ERROR_TEXT = OTP_PROVIDER.get("ERROR_TEXT")
    CELERY = OTP_PROVIDER.get("CELERY")

    def __init__(self):
        super().__init__()

        if self.TRANSPORT not in Transport.all():
            raise ImproperlyConfigured('Please provide valid transport')

        self.TRANSPORT = Transport(self.TRANSPORT)


conf = Conf()
