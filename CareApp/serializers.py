from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'first_name', 'last_name', 'dob', 'address', 'phone_number', 'emergency_contact']

class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = ['id', 'patient', 'care_provider', 'date', 'reason', 'notes']

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ['id', 'encounter', 'observation_type', 'value', 'unit', 'notes', 'timestamp']

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'patient', 'care_provider', 'procedure_name', 'description', 'date', 'outcome']

class CarePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarePlan
        fields = ['id', 'patient', 'care_provider', 'description', 'start_date', 'end_date', 'goals']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'care_plan', 'medication_name', 'dosage', 'frequency', 'start_date', 'end_date']

class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = ['id', 'patient', 'from_care_level', 'to_care_level', 'date', 'notes']

class AuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditTrail
        fields = ['id', 'user', 'action', 'timestamp']
