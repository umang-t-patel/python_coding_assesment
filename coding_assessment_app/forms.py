import datetime

from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    """
    Created two fields in the form as Date and Time will be separate inputs in HTML.
    Added class and type for HTML
    Added Validation to check whether the date is the past date or not.
    """
    appointment_date = forms.DateField(label='Date', widget=forms.DateTimeInput(attrs={
        'class': 'form-control', 'type': 'date'}))
    appointment_time = forms.TimeField(label='Time', widget=forms.DateTimeInput(attrs={
        'class': 'form-control', 'type': 'time'}))

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
        """
        Custom validation to check whether date is a past date or not.
        If it is a past date then it will raise an error message.
        """
        date = self.cleaned_data['appointment_date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
