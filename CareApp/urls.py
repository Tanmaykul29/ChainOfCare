from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from .views import (
    UserRoleView,
    PatientListView,
    PatientDetailView,
    EncounterView,
    ObservationView,
    ProcedureView,
    CarePlanView,
    MedicationView,
    TransitionView,
    AuditTrailView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user-role/', UserRoleView.as_view(), name='user-role'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('encounters/', EncounterView.as_view(), name='encounter-list'),
    path('observations/', ObservationView.as_view(), name='observation-list'),
    path('procedures/', ProcedureView.as_view(), name='procedure-list'),
    path('care-plans/', CarePlanView.as_view(), name='care-plan-list'),
    path('medications/', MedicationView.as_view(), name='medication-list'),
    path('transitions/', TransitionView.as_view(), name='transition-list'),
    path('audit-trails/', AuditTrailView.as_view(), name='audit-trail-list'),
]
