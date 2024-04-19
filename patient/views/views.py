# patient/views/views.py
from rest_framework import generics
from rest_framework.views import APIView
from patient.models.models import Patient, PatientBilling, PatientHistory, PatientLedger, PatientReminder, PatientVisitList
from patient.serializers import (
    PatientSerializer, 
    PatientBillingSerializer, 
    PatientHistorySerializer, 
    PatientLedgerSerializer, 
    PatientReminderSerializer, 
    PatientVisitListSerializer
)
# from ...hos_login.permissions import IsHospitalOwner
from patient.permissions import IsAuthenticatedHospitalOwner
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from hos_login.permissions import IsHospitalOwner  # Import the custom permission class from the login app
from django.http import JsonResponse
from rest_framework.response import Response

# Patient API views

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsHospitalOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Patient.objects.filter(owner=self.request.user)
        search_query = self.request.query_params.get('search', None)
        if search_query:
            if search_query.isdigit():
                queryset = queryset.filter(PatientID=int(search_query))
            else:
                queryset = queryset.filter(fullname__icontains=search_query)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsHospitalOwner] 

# PatientBilling API views
class PatientBillingListCreateView(generics.ListCreateAPIView):
    queryset = PatientBilling.objects.all()
    serializer_class = PatientBillingSerializer

class PatientBillingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientBilling.objects.all()
    serializer_class = PatientBillingSerializer

# PatientHistory API views
class PatientHistoryListCreateView(generics.ListCreateAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

class PatientHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

# PatientLedger API views
class PatientLedgerListCreateView(generics.ListCreateAPIView):
    queryset = PatientLedger.objects.all()
    serializer_class = PatientLedgerSerializer

class PatientLedgerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientLedger.objects.all()
    serializer_class = PatientLedgerSerializer

# PatientReminder API views
class PatientReminderListCreateView(generics.ListCreateAPIView):
    queryset = PatientReminder.objects.all()
    serializer_class = PatientReminderSerializer

class PatientReminderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientReminder.objects.all()
    serializer_class = PatientReminderSerializer

# PatientVisitList API views
class PatientVisitListListCreateView(generics.ListCreateAPIView):
    queryset = PatientVisitList.objects.all()
    serializer_class = PatientVisitListSerializer

class PatientVisitListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientVisitList.objects.all()
    serializer_class = PatientVisitListSerializer
