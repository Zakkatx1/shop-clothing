from django.contrib import admin
from .models import Patient, Doctor, Treatment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'gender']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'experience']

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'diagnosis']