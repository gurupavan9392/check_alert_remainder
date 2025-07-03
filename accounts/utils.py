from django.core.mail import send_mail
from django.conf import settings

def send_email(to_email, message, subject='⏰ Check-in Now'):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )
