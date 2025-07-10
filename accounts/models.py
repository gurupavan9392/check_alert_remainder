# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # Check-in date
    time = models.TimeField(auto_now_add=True)
    checked_in = models.BooleanField(default=False)       # ✅ must exist
    checkin_time = models.TimeField(null=True, blank=True)   # Optional: track time too

    def __str__(self):
        return f"{self.User.username} checked in at {self.time} on {self.date}"


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


