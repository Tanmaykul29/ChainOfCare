from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('care_provider', 'Care Provider'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    fhir_id = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_info = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class CareProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='care_provider_profile')
    specialization = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=150)
    contact_info = models.TextField()

    def __str__(self):
        return self.user.get_full_name()

class Encounter(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='encounters')
    care_provider = models.ForeignKey(CareProvider, on_delete=models.CASCADE, related_name='encounters')
    date = models.DateTimeField()
    type = models.CharField(max_length=50, choices=[
        ('consultation', 'Consultation'),
        ('follow_up', 'Follow-Up'),
        ('emergency', 'Emergency'),
    ])
    notes = models.TextField()

    def __str__(self):
        return f"Encounter on {self.date} for {self.patient}"


class Observation(models.Model):
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='observations')
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    unit = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.type}: {self.value} {self.unit}"


class Procedure(models.Model):
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='procedures')
    procedure_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    outcome = models.TextField()

    def __str__(self):
        return self.procedure_name


class CarePlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='care_plans')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ])

    def __str__(self):
        return f"Care Plan for {self.patient} ({self.status})"


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in days")

    def __str__(self):
        return self.name


class Transition(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='transitions')
    from_care = models.CharField(max_length=100)
    to_care = models.CharField(max_length=100)
    transition_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"Transition from {self.from_care} to {self.to_care}"


class AuditTrail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audit_trails')
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"Audit by {self.user.username} on {self.timestamp}"
