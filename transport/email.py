from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def test_email():
    from apps.core.models import AppSettings
    app_core_settings = AppSettings.load()

    subject = f"Test"

    from_email = app_core_settings.no_reply_email
    to = [app_core_settings.main_email]
    bcc = app_core_settings.get_notification_emails()
    html = render_to_string("base.html", {
    })

    mail = EmailMultiAlternatives(
        subject=subject, body=html, from_email=from_email, to=to, bcc=bcc)

    mail.attach_alternative(html, "text/html")

    return mail.send(fail_silently=True)



