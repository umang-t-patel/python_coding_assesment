from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Appointment
from .forms import AppointmentForm
import datetime


def index(request):
    data = dict()
    return render(request, 'appointment_list.html', {'data': data})

def appointment_list_all_filter(request):
    data = dict()
    if request.method == 'POST':
        search_text = (request.POST['search_text']).strip()
        if search_text:
            appointment = Appointment.objects.filter(appointment_desc__contains=search_text)
        else:
            appointment = Appointment.objects.all()
        appointment_list = appointment_obj_to_list(appointment)
        data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
            'appointments': appointment_list
        })
    else:
        appointment = Appointment.objects.all()
        appointment_list = appointment_obj_to_list(appointment)
        data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
            'appointments': appointment_list
        })
    return JsonResponse(data)


def save_appointment_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.appointment_date_time = datetime.datetime.combine(form.cleaned_data['appointment_date'], form.cleaned_data['appointment_time']) # Set the user object here
            appointment.save()
            data['form_is_valid'] = True
            appointment = Appointment.objects.all()
            appointment_list = appointment_obj_to_list(appointment)
            data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
                'appointments': appointment_list
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def appointment_save(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
    else:
        form = AppointmentForm()
    return save_appointment_form(request, form, 'includes/partial_appointment_save.html')


def appointment_obj_to_list(appointment):
    appointment_list = []
    for appointment_obj in appointment:
        appointment_temp_list = []
        appointment_temp_list.append(appointment_obj.appointment_date_time.date().strftime("%m/%d/%Y"))
        appointment_temp_list.append(appointment_obj.appointment_date_time.strftime("%I:%M %p"))
        appointment_temp_list.append(appointment_obj.appointment_desc)
        appointment_list.append(appointment_temp_list)
    print(appointment_list)
    return appointment_list
