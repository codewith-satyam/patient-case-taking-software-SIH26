
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor
from django.db.models import Q

def register_patient(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        chief_complaint = request.POST.get("chief_complaint", "").strip()
        medical_history = request.POST.get("medical_history", "").strip()
        

        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            mobile=mobile,
            chief_complaint=chief_complaint,
            medical_history=medical_history,
        )

        return redirect("patient_success")

    return render(request, "patients/register.html")


def patient_success(request):
    return render(request, "patients/success.html")


def patient_dashboard(request):
    query = request.GET.get("q", "").strip()

    patients = Patient.objects.all().order_by("-created_at")

    if query:
        patients = patients.filter(name__icontains=query)

    total_patients = Patient.objects.count()

    return render(request, "patients/dashboard.html", {
        "patients": patients,
        "total_patients": total_patients,
        "query": query,
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient


def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(
        request,
        "patients/detail.html",
        {"patient": patient}
    )


def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        patient.name = request.POST.get("name", "").strip()
        patient.age = request.POST.get("age")
        patient.gender = request.POST.get("gender")
        patient.mobile = request.POST.get("mobile", "").strip()
        patient.chief_complaint = request.POST.get(
            "chief_complaint", ""
        ).strip(),
        patient.medical_history = request.POST.get(
    "medical_history", ""
).strip(),

        patient.save()
        return redirect("patient_detail", patient_id=patient.id)

    return render(
        request,
        "patients/edit.html",
        {"patient": patient}
    )



def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        patient.delete()
        return redirect("patient_dashboard")

    return render(
        request,
        "patients/delete.html",
        {"patient": patient}
    )


def register_doctor(request):

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        specialization = request.POST.get("specialization", "").strip()
        mobile = request.POST.get("mobile", "").strip()
        email = request.POST.get("email", "").strip()
        availability = request.POST.get("availability", "Available")

        Doctor.objects.create(
            name=name,
            specialization=specialization,
            mobile=mobile,
            email=email,
            availability=availability
        )

        return redirect("doctor_dashboard")

    return render(request, "patients/doctor_register.html")


def doctor_dashboard(request):
    search_query = request.GET.get("search", "")
    selected_specialization = request.GET.get("specialization", "")

    doctors = Doctor.objects.all().order_by("-created_at")

    if search_query:
        doctors = doctors.filter(
            Q(name__icontains=search_query) |
            Q(specialization__icontains=search_query)
        )

    if selected_specialization:
        doctors = doctors.filter(
            specialization=selected_specialization
        )

    specializations = Doctor.objects.values_list(
        "specialization", flat=True
    ).distinct()

    total_doctors = Doctor.objects.count()

    # Total Specializations
    total_specializations = Doctor.objects.values(
        "specialization"
    ).distinct().count()

    # Latest Registered Doctor
    latest_doctor = Doctor.objects.order_by(
        "-created_at"
    ).first()

    return render(request, "patients/doctor_dashboard.html", {
        "doctors": doctors,
        "total_doctors": total_doctors,
        "search_query": search_query,
        "specializations": specializations,
        "selected_specialization": selected_specialization,
        "total_specializations": total_specializations,
        "latest_doctor": latest_doctor,
    })


def doctor_detail(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    return render(
        request,
        "patients/doctor_detail.html",
        {"doctor": doctor}
    )
def edit_doctor(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":

        doctor.name = request.POST.get("name", "").strip()
        doctor.specialization = request.POST.get("specialization", "").strip()
        doctor.mobile = request.POST.get("mobile", "").strip()
        doctor.email = request.POST.get("email", "").strip()
        doctor.availability = request.POST.get("availability")

        doctor.save()

        return redirect("doctor_detail", doctor_id=doctor.id)

    return render(
        request,
        "patients/edit_doctor.html",
        {"doctor": doctor}
    )

def delete_doctor(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        doctor.delete()
        return redirect("doctor_dashboard")

    return render(
        request,
        "patients/delete_doctor.html",
        {"doctor": doctor}
    )