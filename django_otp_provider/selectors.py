from django.core.exceptions import ObjectDoesNotExist

from .models import Otp


def get_otp_by_key(raise_exc: bool = False, **kwargs):
    otp = Otp.objects.filter(**kwargs).first()
    if otp is None and raise_exc:
        raise ObjectDoesNotExist(f"{Otp.__class__.__name__} instance not found")

    return otp
