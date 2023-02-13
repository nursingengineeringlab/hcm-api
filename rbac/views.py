from django.shortcuts import render

# app/views.py

from django.shortcuts import render
from .models import Patient, Nurse, Admin

def view_patient_data(request, patient_id):
    """
    Get the patient with the given id, and render the patient_data.html template with the patient
    object.
    
    :param request: This is the request object that is sent to the view. It contains information about
    the request, such as the HTTP method, the URL, the headers, and the body
    :param patient_id: This is the id of the patient that we want to view
    :return: The patient data is being returned.
    """
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patient_data.html', {'patient': patient})

def view_group_data(request, nurse_id):
    """
    It takes a request and a nurse_id, gets the nurse with that id, gets all the patients associated
    with that nurse, and then renders the group_data.html template with the nurse and patients as
    context.
    
    :param request: The request object is the first parameter to every view function. It contains
    information about the request that was made to the server, such as the HTTP method, the URL, the
    headers, and the body of the request
    :param nurse_id: the id of the nurse that is logged in
    :return: The nurse and the patients that are assigned to that nurse.
    """
    nurse = Nurse.objects.get(id=nurse_id)
    patients = nurse.patients.all()
    return render(request, 'group_data.html', {'nurse': nurse, 'patients': patients})

def view_all_data(request):
    patients = Patient.objects.all()
    nurses = Nurse.objects.all()
    admins = Admin.objects.all()
    return render(request, 'all_data.html', {'patients': patients, 'nurses': nurses, 'admins': admins})


# --------------------------
# patient user view
def patient_view(request):
    # get the logged in user
    user = request.user
    # get the patient data for the logged in user
    patient_data = Patient.objects.get(user=user)
    # return the patient data
    return render(request, 'patient.html', {'patient_data': patient_data})

# nurse user view
def nurse_view(request):
    # get the logged in user
    user = request.user
    # get the patients assigned to the nurse
    patients = Patient.objects.filter(nurse=user)
    # return the patient data
    return render(request, 'nurse.html', {'patients': patients})

# admin user view
def admin_view(request):
    # get all patient data
    patients = Patient.objects.all()
    # return the patient data
    return render(request, 'admin.html', {'patients': patients})

# -----------------------------
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from rbac.models import User, Patient, Nurse

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = "patients"
    template_name = "rbac/patient_list.html"

# -----------------------------
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def view_data(request):
    user = request.user
    if user.is_superuser:
        # Admin user can view all data
        data = Patient.objects.all()
    elif hasattr(user, 'nurse'):
        # Nurse user can view data of group of patients assigned to the nurse
        data = Patient.objects.filter(nurse=user.nurse)
    else:
        # Patient user can view data of oneself
        data = Patient.objects.filter(pk=user.patient.pk)
    return render(request, 'rbac/data.html', {'data': data})

