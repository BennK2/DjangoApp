from django.urls import path
from . import views
from django.shortcuts import redirect  # ✅ Required import


urlpatterns = [
    path('', lambda request: redirect('login/', permanent=True)),  # Redirect root to login
    path('login/', views.login_view, name='login'),

    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('view-patients/', views.view_patients, name='view_patients'),
    path('update-patient/<int:id>/', views.update_patient, name='update_patient'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('view-doctors/', views.view_doctors, name='view_doctors'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('add-treatment/', views.add_treatment, name='add_treatment'),
    path('view-treatments/', views.view_treatments, name='view_treatments'),

]
