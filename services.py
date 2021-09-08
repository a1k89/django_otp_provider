from typing import Optional

from django.core.exceptions import ValidationError

from .models import Otp
from . import selectors as otp_sel
from .conf import conf
from .utils import send_code


@send_code
def generate_otp(key) -> Optional[Otp]:
    """
    Generate or recreate otp.

    """
    otp = otp_sel.get_otp_by_key(key=key)

    if hasattr(otp, "is_allow_recreate"):
        if otp.is_allow_recreate:
            otp.delete()

    if otp is None:
        return Otp.objects.create(key=key)

    raise ValidationError(conf.ERROR_TEXT)


def verify_otp(key: str, token: str, code: str):
    otp = otp_sel.get_otp_by_key(token=token, key=key, raise_exc=True)

    if not otp.is_allow_new_attempt:
        raise ValidationError(conf.ERROR_TEXT_ATTEMTPS)

    if code != otp.code:
        otp.attempts -= 1
        otp.save()
        raise ValidationError(conf.ERROR_TEXT_CODE)
    else:
        otp.delete()
