from django.contrib import admin
from .models import Patient , Doctor

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('name','age','gender','mobile','created_at')
    search_fields=('name','mobile')
    list_filter=('gender','created_at')
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'mobile', 'email', 'created_at')
    search_fields = ('name', 'specialization', 'mobile')    
    

