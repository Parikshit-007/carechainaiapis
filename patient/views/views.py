# patient/views/views.py
from rest_framework import generics
from rest_framework.views import APIView
from patient.models.models import Patient, PatientBilling, PatientHistory, Visit,PatientLedger, PatientReminder, PatientVisitList
from decimal import Decimal, InvalidOperation

from patient.serializers import (
    PatientSerializer, 
    PatientBillingSerializer, 
    PatientHistorySerializer, 
    PatientLedgerSerializer, 
    PatientReminderSerializer, 
    PatientVisitListSerializer,
    VisitSerializer
)
from rest_framework import status
from knox.auth import TokenAuthentication
# from ...hos_login.permissions import IsHospitalOwner
from patient.permissions import IsAuthenticatedHospitalOwner
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied

from hos_login.permissions import IsHospitalOwner  # Import the custom permission class from the login app
from django.http import JsonResponse
from rest_framework.response import Response

# Patient API views

from rest_framework.exceptions import PermissionDenied
from rest_framework import status, viewsets
from rest_framework.response import Response

class OwnerBasedQuerysetMixin:
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")
        
        queryset = self.queryset.filter(owner=self.request.user)

        # Optional: Adding search functionality if needed
        search_query = self.request.query_params.get('search', None)
        if search_query:
            if search_query.isdigit():
                queryset = queryset.filter(PatientID=int(search_query))
            else:
                queryset = queryset.filter(fullname__icontains=search_query)

        return queryset

class AssignOwnerMixin:
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to perform this action.")
        
        serializer.save(owner=self.request.user)


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
#    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view

    def perform_create(self, serializer):
        # If user is not authenticated, raise an error
        if not self.request.user.is_authenticated:
            return Response({'error': 'Unauthorized access'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Save with the current authenticated user as the owner
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = Patient.objects.filter(owner=self.request.user)

        search_query = self.request.query_params.get('search', None)
        if search_query:
            if search_query.isdigit():
                queryset = queryset.filter(PatientID=int(search_query))
            else:
                queryset = queryset.filter(fullname__icontains=search_query)

        return queryset

    def list(self, request, *args, **kwargs):
        # Check if the user is authenticated before listing
        if not self.request.user.is_authenticated:
            return Response({'error': 'Unauthorized access'}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class PatientRetrieveUpdateDestroyView(OwnerBasedQuerysetMixin, AssignOwnerMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated] 

# PatientBilling API views
class PatientBillingListCreateView(OwnerBasedQuerysetMixin, AssignOwnerMixin,generics.ListCreateAPIView):
    queryset = PatientBilling.objects.all()
    serializer_class = PatientBillingSerializer

class PatientBillingRetrieveUpdateDestroyView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientBilling.objects.all()
    serializer_class = PatientBillingSerializer

# PatientHistory API views
class PatientHistoryListCreateView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.ListCreateAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

class PatientHistoryRetrieveUpdateDestroyView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

# PatientLedger API views
class PatientLedgerListCreateView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.ListCreateAPIView):
    queryset = PatientLedger.objects.all()
    serializer_class = PatientLedgerSerializer

class PatientLedgerRetrieveUpdateDestroyView(OwnerBasedQuerysetMixin, AssignOwnerMixin ,generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientLedger.objects.all()
    serializer_class = PatientLedgerSerializer

# PatientReminder API views
class PatientReminderListCreateView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.ListCreateAPIView):
    queryset = PatientReminder.objects.all()
    serializer_class = PatientReminderSerializer

class PatientReminderRetrieveUpdateDestroyView(OwnerBasedQuerysetMixin, AssignOwnerMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientReminder.objects.all()
    serializer_class = PatientReminderSerializer

# PatientVisitList API views
class PatientVisitListListCreateView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.ListCreateAPIView):
    queryset = PatientVisitList.objects.all()
    serializer_class = PatientVisitListSerializer
 #   authentication_classes = (TokenAuthentication,)
from django.db.models import Sum

class PatientVisitListRetrieveUpdateDestroyView(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientVisitList.objects.all()
    serializer_class = PatientVisitListSerializer
  #  authentication_classes = (TokenAuthentication,)
class VisitViewSet(generics.ListCreateAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Visit.objects.all()

    def get_queryset(self):
        return Visit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     # Create a mutable copy of the request data
    #     data = dict(request.data)  # Convert QueryDict to a dict

    #     # Debugging: Print the request data
    #     print("Request data (mutable):", data)

    #     # Extract data fields
    #     patient_id = data.get('patient')
    #     total_visits = int(data.get('total_visits', 0))  # Ensure total_visits is an integer

    #     if not patient_id:
    #         return Response({'error': 'Patient ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    #     # Add owner to the data
    #     data['owner'] = request.user.pk

    #     # Create the serializer instance with the updated data
    #     serializer = self.get_serializer(data=data)

    #     # Validate the serializer data
    #     if not serializer.is_valid():
    #         print("Serializer errors:", serializer.errors)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     # Save the validated serializer data
    #     self.perform_create(serializer)

    #     # Calculate total cost using manually provided total_visits
    #     doctor_id = serializer.validated_data.get('doctor')
    #     visit_price = serializer.validated_data.get('price', 0)
    #     total_cost = total_visits * visit_price

    #     response_data = {
    #         'visit': serializer.data,
    #         'total_visits': total_visits,
    #         'total_cost': total_cost
    #     }

    #     # Return a success response with the created data and calculated fields
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    
class VisitViewSet(OwnerBasedQuerysetMixin, AssignOwnerMixin, generics.ListCreateAPIView):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]
    queryset = Visit.objects.all()  

    def get_queryset(self):
        return Visit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

   