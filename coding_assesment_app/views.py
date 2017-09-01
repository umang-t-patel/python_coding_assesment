from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Appointment
from .forms import AppointmentForm


def appointment_list(request):
    appointment = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointment})


def save_appointment_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            appointment = Appointment.objects.all()
            data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
                'appointments': appointment
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


def appointment_search(request):
    data = dict()
    search_text = (request.POST['search_text']).strip()
    if request.method == 'POST':
        if search_text:
            appointment = Appointment.objects.filter(appointment_desc__contains=search_text)
            data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
                'appointments': appointment
            })
        else:
            appointment = Appointment.objects.all()
            data['html_appointment_list'] = render_to_string('includes/partial_appointment_list.html', {
                'appointments': appointment
            })
    return JsonResponse(data)
