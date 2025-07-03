import sys
import os

# ✅ Add the project base directory (where manage.py is) to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ✅ Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkin_remainder.settings')

# ✅ Setup Django
import django
django.setup()

import os
import django
from datetime import date
from django.utils.timezone import localtime

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkin_remainder.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import CheckIn
from accounts.utils import send_email

# Get current time and date
now = localtime().time()
today = date.today()

# 🔔 10:25 AM Reminder
if now.hour == 10 and now.minute == 25:
    print("⏰ Sending 10:25 AM check-in reminder emails...")
    for user in User.objects.all():
        if user.email:
            message = f"""
Hi {user.username},

Please go and check in now. ✅

– Your Check-In App
"""
            send_email(
                to_email=user.email,
                subject="⏰ Check-in Reminder",
                message=message
            )
            print(f"✅ Email sent to {user.email}")

# 🚨 After 10:30 AM Missed Alert
elif now.hour == 10 and now.minute >= 30:
    print("🚨 Checking for missed check-ins...")
    for user in User.objects.all():
        if user.email and not CheckIn.objects.filter(user=user, date=today).exists():
            message = f"""
Hi {user.username},

You missed your check-in today. ⏱️  
Please try to be on time tomorrow.

– Your Check-In App
"""
            send_email(
                to_email=user.email,
                subject="❗Missed Check-in Alert",
                message=message
            )
            print(f"🚨 Missed check-in email sent to {user.email}")

# 🕒 Any other time
else:
    print("⏳ Not 10:25 or 10:30+ — no email sent.")

