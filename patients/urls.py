
from django.urls import path
from . import views

urlpatterns = [
    path("", views.register_patient, name="register_patient"),
    path("success/", views.patient_success, name="patient_success"),
    path("dashboard/", views.patient_dashboard, name="patient_dashboard"),
    path("patient/<int:patient_id>/",views.patient_detail,name="patient_detail"),
    path("patient/<int:patient_id>/edit/",views.edit_patient,name="edit_patient"),

    path("patient/<int:patient_id>/delete/",views.delete_patient,name="delete_patient"),
    path("doctor/register/",views.register_doctor,name="register_doctor"),
    path("doctors/",views.doctor_dashboard,name="doctor_dashboard"),
    path(
    "doctor/<int:doctor_id>/",
    views.doctor_detail,
    name="doctor_detail"
),
path(
    "doctor/<int:doctor_id>/edit/",
    views.edit_doctor,
    name="edit_doctor"
),
path(
    "doctor/<int:doctor_id>/delete/",
    views.delete_doctor,
    name="delete_doctor"
),

]
