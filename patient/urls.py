# patient/urls.py
from django.urls import path,include
from patient.views.views import (
    PatientListCreateView, PatientRetrieveUpdateDestroyView,
    PatientBillingListCreateView, PatientBillingRetrieveUpdateDestroyView,
    PatientHistoryListCreateView, PatientHistoryRetrieveUpdateDestroyView,
    PatientLedgerListCreateView, PatientLedgerRetrieveUpdateDestroyView,
    PatientReminderListCreateView, PatientReminderRetrieveUpdateDestroyView,
    PatientVisitListListCreateView, PatientVisitListRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('api/auth/', include('hos_login.urls')),
   # patient_dashboard
    path('api/patients/', PatientListCreateView.as_view(), name='api-patient-list-create'),
    path('api/patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='api-patient-retrieve-update-destroy'),

    path('api/patient-billings/', PatientBillingListCreateView.as_view(), name='api-patientbilling-list-create'),
    path('api/patient-billings/<int:pk>/', PatientBillingRetrieveUpdateDestroyView.as_view(), name='api-patientbilling-retrieve-update-destroy'),

    path('api/patient-histories/', PatientHistoryListCreateView.as_view(), name='api-patienthistory-list-create'),
    path('api/patient-histories/<int:pk>/', PatientHistoryRetrieveUpdateDestroyView.as_view(), name='api-patienthistory-retrieve-update-destroy'),

    path('api/patient-ledgers/', PatientLedgerListCreateView.as_view(), name='api-patientledger-list-create'),
    path('api/patient-ledgers/<int:pk>/', PatientLedgerRetrieveUpdateDestroyView.as_view(), name='api-patientledger-retrieve-update-destroy'),

    path('api/patient-reminders/', PatientReminderListCreateView.as_view(), name='api-patientreminder-list-create'),
    path('api/patient-reminders/<int:pk>/', PatientReminderRetrieveUpdateDestroyView.as_view(), name='api-patientreminder-retrieve-update-destroy'),

    path('api/patient-visitlists/', PatientVisitListListCreateView.as_view(), name='api-patientvisitlist-list-create'),
    path('api/patient-visitlists/<int:pk>/', PatientVisitListRetrieveUpdateDestroyView.as_view(), name='api-patientvisitlist-retrieve-update-destroy'),
]
