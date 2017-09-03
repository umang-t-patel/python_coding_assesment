from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    """
    Stores appointment_date_time (Appointment Date with Time) and appointment_desc (Appointment description)
    """
    appointment_date_time = models.DateTimeField(default=timezone.now)
    appointment_desc = models.CharField(max_length=100)
