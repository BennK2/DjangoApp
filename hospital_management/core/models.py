from django.db import models

# This class represents a patient in the hospital.
# Defines a Django model for storing patient details in the database.
class Patient(models.Model):
    full_name = models.CharField(max_length=100)  # A text field for the patient's name, up to 100 characters.
    gender = models.CharField(max_length=10)      # A text field for gender, up to 10 characters.
    date_of_birth = models.DateField()            # A date field for the patient's birth date.
    contact_number = models.CharField(max_length=15)  # A text field for the patient's contact number, up to 15 characters.

    # Returns the string representation of the object, typically used in admin panels and debugging.
    def __str__(self):
        # Returns the value of the 'full_name' attribute when the object is converted to a string.
        return self.full_name

# Defines a Django model for storing doctor details in the database.
class Doctor(models.Model):
    name = models.CharField(max_length=100)           # A text field for the doctor's name, up to 100 characters.
    department = models.CharField(max_length=50)      # A text field for the department, up to 50 characters.
    contact_email = models.EmailField()               # An email field for the doctor's contact email.

    # Returns the string representation of the object, typically used in admin panels and debugging.
    def __str__(self):
        # Returns the value of the 'name' attribute when the object is converted to a string.
        return self.name

# Defines a Django model for storing appointment records.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # ForeignKey to Patient; deletes appointments if the patient is deleted.
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)    # ForeignKey to Doctor; deletes appointments if the doctor is deleted.
    appointment_date = models.DateField()                           # A date field for when the appointment happens.
    reason = models.CharField(max_length=200)                       # A text field for the appointment reason, up to 200 characters.

    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.appointment_date}"

# Defines a Django model for storing treatment details linked to appointments.
class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  # ForeignKey to Appointment; deletes treatments if the appointment is deleted.
    diagnosis = models.CharField(max_length=200)                            # A text field for the diagnosis, up to 200 characters.
    prescription = models.CharField(max_length=200)                         # A text field for the prescription, up to 200 characters.
    notes = models.TextField()                                              # A text field for additional notes.

    def __str__(self):
        return f"Treatment for {self.appointment}"

# Model for user signup (registration)
class Signup(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Unique username
    email = models.EmailField(unique=True)                    # Unique email
    pa***MASKED*** = \"******\"odels.CharField(max_length=128)               # Hashed pa***MASKED***

    def __str__(self):
        return self.username

# Model for user login (for storing login attempts or sessions, optional)
class Login(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)  # Reference to the Signup user
    login_time = models.DateTimeField(auto_now_add=True)        # Timestamp of login

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"
    
# Model for user logout (for tracking logout events, optional)
class Logout(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)  # Reference to the Signup user
    logout_time = models.DateTimeField(auto_now_add=True)       # Timestamp of logout

    def __str__(self):
        return f"{self.user.username} logged out at {self.logout_time}"