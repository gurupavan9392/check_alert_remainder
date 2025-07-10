import sys
import os
from datetime import date
from django.utils.timezone import localtime

# ✅ Setup Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkin_remainder.settings')

import django
django.setup()

from django.contrib.auth.models import User
from accounts.models import CheckIn
from accounts.utils import send_email

# ✅ Get current time and date
now = localtime().time()
today = date.today()

# 🔔 8:50 AM Reminder
if now.hour == 8 and now.minute == 50:
    print("⏰ Sending 8:50 AM check-in reminder emails...")
    for user in User.objects.all():
        if user.email:
            message = f"""
Hi {user.username},

Good morning! 🌞  
Please don't forget to check in at 9:00 AM. ✅

– Your Check-In App
"""
            send_email(
                to_email=user.email,
                subject="⏰ Check-in Reminder: 9:00 AM",
                message=message
            )
            print(f"✅ Reminder email sent to {user.email}")

# 🚨 After 9:00 AM Missed Alert
elif now.hour == 9 and now.minute >= 1:
    print("🔍 Checking for missed check-ins after 9:00 AM...")
    for user in User.objects.all():
        if user.email and not CheckIn.objects.filter(user=user, date=today).exists():
            message = f"""
Hi {user.username},

You missed your 9:00 AM check-in today. ⏱️  
Please make sure to check in on time tomorrow.

– Your Check-In App
"""
            send_email(
                to_email=user.email,
                subject="❌ Missed Check-in Alert",
                message=message
            )
            print(f"🚨 Missed check-in email sent to {user.email}")

else:
    print("⏳ Not 8:50 or 9:00+ — no email sent.")
