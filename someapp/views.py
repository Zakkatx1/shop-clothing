from django.shortcuts import render
from .models import Patient, Doctor, Treatment

def index(request):
    return render(request, 'index.html')

def patients_table(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

def doctors_table(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def treatments_table(request):
    treatments = Treatment.objects.all()
    return render(request, 'treatments.html', {'treatments': treatments})