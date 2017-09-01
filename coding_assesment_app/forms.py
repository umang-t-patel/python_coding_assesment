from django import forms
from .models import Appointment
import datetime


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'appointment_time', 'appointment_desc',)
        widgets = {
            'appointment_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'appointment_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'appointment_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'appointment_date': 'Date',
            'appointment_time': 'Time',
            'appointment_desc': 'Description',
        }

    def clean_appointment_date(self):
        date = self.cleaned_data['appointment_date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
