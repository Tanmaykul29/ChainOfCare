from django.contrib.auth import get_user_model
from datetime import date, datetime
from models import *;
# Reuse the same admin user (if not created before)
admin_user = get_user_model().objects.get(username='admin')

# Create a third patient user (Chronic Kidney Disease patient)
patient_user_3 = get_user_model().objects.create_user(
    username='patient3',
    email='patient3@example.com',
    password='patientpassword123',
    role='patient',
    first_name='Ravi',
    last_name='Kumar'
)

# Create care provider users (Nephrologist)
care_provider_user_5 = get_user_model().objects.create_user(
    username='care_provider5',
    email='care_provider5@example.com',
    password='providerpassword123',
    role='care_provider',
    first_name='Dr. Meera',
    last_name='Patel'
)

# Create care provider users (Dialysis Specialist)
care_provider_user_6 = get_user_model().objects.create_user(
    username='care_provider6',
    email='care_provider6@example.com',
    password='dialysispassword123',
    role='care_provider',
    first_name='Dr. Ajay',
    last_name='Singh'
)

# Create a Patient profile for Ravi Kumar (Chronic Kidney Disease patient)
patient_3 = Patient.objects.create(
    user=patient_user_3,
    fhir_id='FHIR78901',
    date_of_birth=date(1970, 5, 10),
    gender='Male',
    contact_info='+91 9876541230, ravi.kumar@example.com',
    address='14, Green Park, Delhi, India'
)

# Create a CareProvider profile for Dr. Meera Patel (Nephrologist)
care_provider_5 = CareProvider.objects.create(
    user=care_provider_user_5,
    specialization='Nephrology',
    hospital_name='AIIMS, Delhi',
    contact_info='+91 9812341234'
)

# Create a CareProvider profile for Dr. Ajay Singh (Dialysis Specialist)
care_provider_6 = CareProvider.objects.create(
    user=care_provider_user_6,
    specialization='Dialysis',
    hospital_name='Max Super Speciality Hospital, Delhi',
    contact_info='+91 9812341235'
)

# Create an Encounter for Patient with Dr. Meera Patel (Initial Consultation)
encounter_5 = Encounter.objects.create(
    patient=patient_3,
    care_provider=care_provider_5,
    date=datetime(2024, 4, 5, 11, 0),
    type='consultation',
    notes='Patient complaining of swelling in legs and fatigue. Diagnosed with Chronic Kidney Disease (CKD).'
)

# Create an Encounter for Patient with Dr. Ajay Singh (Dialysis Consultation)
encounter_6 = Encounter.objects.create(
    patient=patient_3,
    care_provider=care_provider_6,
    date=datetime(2024, 4, 7, 9, 30),
    type='consultation',
    notes='Patient started on regular dialysis. Discussed dialysis options and frequency.'
)

# Create a Procedure for dialysis initiation (if applicable)
procedure_3 = Procedure.objects.create(
    encounter=encounter_6,
    procedure_name='Hemodialysis Initiation',
    date=datetime(2024, 4, 7, 10, 0),
    outcome='Patient initiated on hemodialysis, will require weekly sessions.'
)

# Create Medications prescribed for the patient
medication_9 = Medication.objects.create(
    patient=patient_3,
    name='Amlodipine',
    dosage='5mg',
    frequency='once daily',
    duration=180  # Ongoing for 6 months
)

medication_10 = Medication.objects.create(
    patient=patient_3,
    name='Erythropoietin',
    dosage='10000 IU',
    frequency='weekly',
    duration=365  # Ongoing for 1 year
)

medication_11 = Medication.objects.create(
    patient=patient_3,
    name='Calcium Carbonate',
    dosage='500mg',
    frequency='three times a day',
    duration=365  # Ongoing for 1 year
)

medication_12 = Medication.objects.create(
    patient=patient_3,
    name='Vitamin D3',
    dosage='1000 IU',
    frequency='daily',
    duration=365  # Ongoing for 1 year
)

# Create a Care Plan for the patient
care_plan_3 = CarePlan.objects.create(
    patient=patient_3,
    description='Chronic Kidney Disease management plan with dialysis and medications.',
    start_date=date(2024, 4, 5),
    status='active'
)

# Create a Transition from AIIMS to Max Hospital for Dialysis treatment
transition_3 = Transition.objects.create(
    patient=patient_3,
    from_care='AIIMS, Delhi',
    to_care='Max Super Speciality Hospital, Delhi',
    transition_date=date(2024, 4, 7),
    notes='Transferred to Max Hospital for regular dialysis treatment.'
)

# Create an Audit Trail for the creation of patient and related records
audit_trail_3 = AuditTrail.objects.create(
    user=admin_user,
    action='Created patient profile for Ravi Kumar, assigned nephrologist and dialysis specialist, prescribed medications, and initiated dialysis.',
    timestamp=datetime.now(),
    details='Patient Ravi Kumar diagnosed with Chronic Kidney Disease (CKD) and started dialysis treatment.'
)

# Add Observations for the encounters

# Observation for initial consultation with Dr. Meera Patel (encounter_5)
observation_9 = Observation.objects.create(
    encounter=encounter_5,
    type='Serum Creatinine',
    value='3.2 mg/dL',
    unit='mg/dL',
    date=datetime(2024, 4, 5, 11, 30)
)

# Observation for initial consultation with Dr. Meera Patel (encounter_5)
observation_10 = Observation.objects.create(
    encounter=encounter_5,
    type='Urine Test',
    value='Proteinuria positive',
    unit='N/A',
    date=datetime(2024, 4, 5, 12, 0)
)

# Observation for dialysis consultation with Dr. Ajay Singh (encounter_6)
observation_11 = Observation.objects.create(
    encounter=encounter_6,
    type='Dialysis Access Site',
    value='AV Fistula successful',
    unit='N/A',
    date=datetime(2024, 4, 7, 10, 15)
)

# Observation for post-dialysis monitoring (encounter_6)
observation_12 = Observation.objects.create(
    encounter=encounter_6,
    type='Post-Dialysis Blood Pressure',
    value='120/80 mmHg',
    unit='mmHg',
    date=datetime(2024, 4, 7, 12, 0)
)

print("Sample data for Ravi Kumar created successfully!")
