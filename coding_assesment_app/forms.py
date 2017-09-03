from django import forms
from .models import Appointment
import datetime


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(label='Date',widget=forms.DateTimeInput(attrs={
            'class':'form-control','type':'date'}))
    appointment_time = forms.TimeField(label='Time',widget=forms.DateTimeInput(attrs={
            'class':'form-control','type':'time'}))
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'appointment_time', 'appointment_desc',)
        widgets = {
            'appointment_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'appointment_desc': 'Description',
        }

    def clean_appointment_date(self):
        date = self.cleaned_data['appointment_date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
