from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Patient, Doctor, Appointment, Treatment

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pa***MASKED*** = \"******\"equest.POST['pa***MASKED***']
        user = authenticate(request, username=username, pa***MASKED***=\"******\"assword)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect  ('login')

def dashboard_view(request):
    context = {
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'appointment_count': Appointment.objects.count(),
        'treatment_count': Treatment.objects.count(),
    }
    return render(request, 'dashboard.html', context)

def add_patient(request):
    if request.method == 'POST':
        Patient.objects.create(
            full_name=request.POST['full_name'],
            gender=request.POST['gender'],
            date_of_birth=request.POST['date_of_birth'],
            contact_number=request.POST['contact_number']
        )
        return redirect('view_patients')
    return render(request, 'add_patient.html')

def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'view_patients.html', {'patients': patients})

def update_patient(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.contact_number = request.POST['contact_number']
        patient.save()
        return redirect('view_patients')
    return render(request, 'update_patient.html', {'patient': patient})

def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('view_patients')
    return render(request, 'delete_patient.html', {'patient': patient})

def add_doctor(request):
    if request.method == 'POST':
        Doctor.objects.create(
            name=request.POST['name'],
            department=request.POST['department'],
            contact_email=request.POST['contact_email']
        )
        return redirect('view_doctors')
    return render(request, 'add_doctor.html')

def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'view_doctors.html', {'doctors': doctors})

def add_appointment(request):
    if request.method == 'POST':
        Appointment.objects.create(
            patient_id=request.POST['patient_id'],
            doctor_id=request.POST['doctor_id'],
            appointment_date=request.POST['appointment_date'],
            reason=request.POST['reason']
        )
        return redirect('view_appointments')
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'add_appointment.html', {'patients': patients, 'doctors': doctors})

def view_appointments(request):
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'view_appointments.html', {'appointments': appointments})

def add_treatment(request):
    if request.method == 'POST':
        Treatment.objects.create(
            appointment_id=request.POST['appointment_id'],
            diagnosis=request.POST['diagnosis'],
            prescription=request.POST['prescription'],
            notes=request.POST['notes']
        )
        return redirect('view_treatments')
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'add_treatment.html', {'appointments': appointments})

def view_treatments(request):
    treatments = Treatment.objects.select_related('appointment__patient', 'appointment__doctor').all()
    return render(request, 'view_treatments.html', {'treatments': treatments})
