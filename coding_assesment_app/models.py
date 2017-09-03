from django.db import models
from django.utils import timezone


# Create your models here.
class Appointment(models.Model):
    appointment_date_time = models.DateTimeField(default=timezone.now)
    appointment_desc = models.CharField(max_length=100)
