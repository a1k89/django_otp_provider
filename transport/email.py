from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .base import BaseTransport


class EmailTransport(BaseTransport):
    def send_code(self):
        subject = 'Auth code'
        from_email = 'test@test.ru'
        to = ['akoptev1989@ya.ru']
        html = render_to_string("base.html", {'otp': self.otp})

        mail = EmailMultiAlternatives(
            subject=subject, body=html, from_email=from_email, to=to )

        mail.attach_alternative( html, "text/html" )

        return mail.send( fail_silently=True )


