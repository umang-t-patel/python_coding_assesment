import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import AppointmentForm
from .models import Appointment


def index(request):
    """
    This is the default method which loads the appointment_list.html
    """
    data = dict()
    return render(request, 'appointment_list.html', {'data': data})


def appointment_list_all_filter(request):
    """
    This method retrieves the data from the database based on the filters.
        1. If input text is blank then retrieve all data.
        2. If input text is not blank then retrieve all data which contains input text
    """
    data = dict()
    if request.method == 'POST':
        search_text = (request.POST['search_text']).strip()
        if search_text:
            # Filter the data using search_text
            appointment = Appointment.objects.filter(appointment_desc__contains=search_text)
        else:
            # Retrieve all data
            appointment = Appointment.objects.all()
        appointment_list = appointment_obj_to_list(appointment)
        data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
            'appointments': appointment_list
        })
    else:
        # Retrieve all data
        appointment = Appointment.objects.all()
        appointment_list = appointment_obj_to_list(appointment)
        data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
            'appointments': appointment_list
        })
    return JsonResponse(data)


def appointment_save(request):
    """
    This method saves the form.
    The date and time is combined together to save it in datetime field.
    Once the form is saved it retrieves all the date to show updated list of data.
    """
    data = dict()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # As we want to save date and time together as datetime we can save form but without committing it.
            # Use commit=False to save it without committing to database.
            appointment = form.save(commit=False)
            # Update appointment_date_time using appointment_date and appointment_time.
            appointment.appointment_date_time = datetime.datetime.combine(form.cleaned_data['appointment_date'],
                                                                          form.cleaned_data['appointment_time'])
            # Save form once appointment_date_time is updated.
            appointment.save()
            data['form_is_valid'] = True
            appointment = Appointment.objects.all()
            appointment_list = appointment_obj_to_list(appointment)
            data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
                'appointments': appointment_list
            })
        else:
            data['form_is_valid'] = False
    else:
        form = AppointmentForm()
    context = {'form': form}
    data['html_form'] = render_to_string('includes/partial_appointment_save.html', context, request=request)
    return JsonResponse(data)


def appointment_obj_to_list(appointment):
    """
    Create a list of appointments data from the appointment object
    :param appointment: Appointment object
    :return: appointment_list
    """
    appointment_list = []
    for appointment_obj in appointment:
        appointment_temp_list = [appointment_obj.appointment_date_time.date().strftime("%m/%d/%Y"),
                                 appointment_obj.appointment_date_time.strftime("%I:%M %p"),
                                 appointment_obj.appointment_desc]
        appointment_list.append(appointment_temp_list)
    return appointment_list
