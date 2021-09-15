import importlib

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from . import utils as otp_utils


OTP_PROVIDER = getattr(settings, "OTP_PROVIDER", {})
OTP_PROVIDER.setdefault("OTP_SIZE", 4)
OTP_PROVIDER.setdefault("DEBUG_OTP_CODE", "1111")
OTP_PROVIDER.setdefault("ATTEMPTS", 3)
OTP_PROVIDER.setdefault("LIFETIME", 60)
OTP_PROVIDER.setdefault("TRANSPORT_TYPE", otp_utils.Transport.SMS)
OTP_PROVIDER.setdefault("TRANSPORT_CLASS")
OTP_PROVIDER.setdefault("ERROR_TEXT", "Please try again later")
OTP_PROVIDER.setdefault("ERROR_TEXT_CODE", "Code is not valid")
OTP_PROVIDER.setdefault("ERROR_TEXT_ATTEMTPS", "No attempts left")
OTP_PROVIDER.setdefault("CELERY", "run_celery")


class Conf:
    OTP_SIZE = OTP_PROVIDER.get("OTP_SIZE")
    ATTEMPTS = OTP_PROVIDER.get("ATTEMPTS")
    LIFETIME = OTP_PROVIDER.get("LIFETIME")
    DEBUG_OTP_CODE = OTP_PROVIDER.get("DEBUG_OTP_CODE")
    TRANSPORT_TYPE = OTP_PROVIDER.get("TRANSPORT_TYPE")
    TRANSPORT_CLASS = OTP_PROVIDER.get("TRANSPORT_CLASS")
    ERROR_TEXT = OTP_PROVIDER.get("ERROR_TEXT")
    ERROR_TEXT_CODE = OTP_PROVIDER.get("ERROR_TEXT_CODE")
    ERROR_TEXT_ATTEMTPS = OTP_PROVIDER.get("ERROR_TEXT_ATTEMTPS")
    CELERY = OTP_PROVIDER.get("CELERY")

    @classmethod
    def resolve_transport(cls, transport):
        try:
           return otp_utils.Transport(transport)
        except ValueError:
            raise ImproperlyConfigured("Transport is not defined")

    @classmethod
    def resolve_provider(cls, path: str):
        arr = path.split('.')
        class_obj = arr.pop()
        try:
            module = importlib.import_module('.'.join(arr))
        except ModuleNotFoundError:
            raise ImproperlyConfigured("TRANSPORT_CLASS value is not valid")

        if not hasattr(module, class_obj):
            raise ImproperlyConfigured(f"class {class_obj} not found in module {module}")

        return getattr(module, class_obj)

    def __init__(self):
        self.TRANSPORT_TYPE = self.__class__.resolve_transport(self.TRANSPORT_TYPE)
        self.TRANSPORT_CLASS = self.__class__.resolve_provider(self.TRANSPORT_CLASS)


conf = Conf()
