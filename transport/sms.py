from .base import BaseTransport


class SmsTransport(BaseTransport):
    def send_code(self):
        print(f'send sms code {self.otp.code}')
