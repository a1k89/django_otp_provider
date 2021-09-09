import random
from django.test import TestCase
from django.core.exceptions import ValidationError

from django_otp_provider.lib.services import verify_otp
from django_otp_provider.lib.models import Otp


class VerifyOtpTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.key = random.randint(1000000000, 9999999999)

    def test_with_correct_data(self):
        otp_db = Otp.objects.create(
            key=self.key
        )
        otp = verify_otp(key=otp_db.key,
                         token=otp_db.token,
                         code=otp_db.code)
        self.assertIsNone(otp)

    def test_wrong_data(self):
        otp_db = Otp.objects.create(
            key=self.key
        )

        wrong_code = random.randint(1000, 9000)
        with self.assertRaises(ValidationError):
            verify_otp(key=otp_db.key,
                        token=otp_db.token,
                        code=wrong_code)
