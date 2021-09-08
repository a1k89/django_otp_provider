import uuid
import jwt

from django.db import models
from django.utils import timezone
from django.conf import settings

from .utils import expire_at

from .conf import conf

from django.core.validators import validate_email


class Otp(models.Model):
    """
    The base otp model
    token: send to client
    key: phone number or email
    expire_at: date of code dead
    attempts: number of attempts (try to type code)

    """

    token = models.UUIDField(max_length=250, unique=True, default=uuid.uuid4)
    key = models.CharField(
        max_length=50, unique=True, validators=[conf.TRANSPORT_TYPE.validator]
    )
    expire_at = models.DateTimeField(default=expire_at)
    attempts = models.PositiveIntegerField(default=conf.ATTEMPTS)
    is_code_sended = models.BooleanField(default=False)

    def __repr__(self):
        return self.token

    class Meta:
        unique_together = ['token', 'key',]

    @property
    def is_allow_recreate(self):
        return timezone.now() >= self.expire_at

    @property
    def is_allow_new_attempt(self):
        return self.attempts > 0

    @property
    def code(self) -> str:
        if settings.DEBUG:
            return conf.DEBUG_OTP_CODE

        payload = {"token": str(self.token), "key": str(self.key)}
        encode = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        numbers = [n for n in reversed(encode) if n.isdigit()]
        repr_str = "".join(numbers[: conf.OTP_SIZE])

        while len(repr_str) < conf.OTP_SIZE:
            repr_str = "0" + repr_str

        return repr_str
