from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('patients/', views.patients_table),
    path('doctors/', views.doctors_table),
    path('treatments/', views.treatments_table),
]