import random
from django.test import TestCase
from django.core.exceptions import ValidationError

from django_otp_provider.lib.services import generate_otp


class GenerateOtpTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.key = random.randint(1000000000, 9999999999)

    def test_correct_value(self):
        otp = generate_otp(key=self.key)
        self.assertIsNotNone(otp.pk)

    def test_send_key_twice(self):
        with self.assertRaises(ValidationError):
            [generate_otp(key=self.key) for _ in range(2)]
