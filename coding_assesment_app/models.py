from django.db import models
from django.utils import timezone


# Create your models here.
class Appointment(models.Model):
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField(default=timezone.now)
    appointment_desc = models.CharField(max_length=100)
