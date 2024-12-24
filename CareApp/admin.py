from django.contrib import admin
from .models import (
    User,
    Patient,
    Encounter,
    Observation,
    Procedure,
    CarePlan,
    Medication,
    Transition,
    AuditTrail,
)

# Register each model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'is_active')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_first_name', 'user_last_name', 'date_of_birth')
    search_fields = ('user__first_name', 'user__last_name', 'user__username')
    list_filter = ('date_of_birth',)

    # Adding methods to show first_name and last_name from the related User model
    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name


@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('patient', 'care_provider', 'date', 'type')
    search_fields = ('patient__first_name', 'care_provider__user__username', 'type')
    list_filter = ('date',)

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('encounter', 'type', 'value', 'unit', 'date')
    search_fields = ('encounter__patient__first_name', 'type')
    list_filter = ('date',)

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('encounter', 'procedure_name', 'date', 'outcome')
    search_fields = ('procedure_name', 'encounter__patient__first_name')
    list_filter = ('date',)

@admin.register(CarePlan)
class CarePlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'description', 'start_date', 'end_date', 'status')
    search_fields = ('patient__first_name', 'description', 'status')
    list_filter = ('status',)

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'dosage', 'frequency', 'duration')
    search_fields = ('name', 'patient__first_name')
    list_filter = ('duration',)

@admin.register(Transition)
class TransitionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'from_care', 'to_care', 'transition_date')
    search_fields = ('patient__first_name', 'from_care', 'to_care')
    list_filter = ('transition_date',)

@admin.register(AuditTrail)
class AuditTrailAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp', 'details')
    search_fields = ('user__username', 'action')
    list_filter = ('timestamp',)
