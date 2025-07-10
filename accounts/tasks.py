from celery import shared_task
from datetime import datetime
from .models import CheckIn
from .utils import send_email  

@shared_task
def send_pre_checkin_alert(user_id):
    today = datetime.today().date()
    checkin = CheckIn.objects.filter(user__id=user_id, date=today).first()
    if checkin:
        email = checkin.user.email
        name = checkin.user.username
        subject = " Check-in Reminder"
        message = f"Hi {name}, your check-in is at 9:00 AM. Please don’t forget."
        send_email(email, subject, message)

@shared_task
def send_post_checkin_alert(user_id):
    today = datetime.today().date()
    checkin = CheckIn.objects.filter(user__id=user_id, date=today, checked_in=False).first()
    if checkin:
        email = checkin.user.email
        name = checkin.user.username
        subject = " Missed Check-in"
        message = f"Hi {name}, you missed your 9:00 AM check-in!"
        send_email(email, subject, message)
