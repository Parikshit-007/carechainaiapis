# views.py
from django.http import Http404
from rest_framework import generics
from ipd.models.models import (
    BedAllocation, BedAvailability, BedBooking, BedStatusUpdate, IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport, 
    IPDDepositReport, IPDDischargeReport, DepartmentReport, Ward, 
    WardWiseReport, DoctorWiseReport, TPAReport, Bed,DischargeHistory
) 
from ipd.models.models import Bed
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.db import transaction

from ipd.serializers import (
    IPDRegistrationSerializer, IPDDepositSerializer, IPDDischargeSerializer, 
    IPDAdmitReportSerializer, IPDDepositReportSerializer, IPDDischargeReportSerializer,
    DepartmentReportSerializer, WardSerializer, WardWiseReportSerializer, DoctorWiseReportSerializer, TPAReportSerializer , BedSerializer, BedBookingSerializer, BedAllocationSerializer, \
    BedStatusUpdateSerializer, BedAvailabilitySerializer,DischargeHistorySerializer
)
from rest_framework import status
from rest_framework.response import Response

from django.db import transaction

class IPDRegistrationListCreateView(generics.ListCreateAPIView):
    serializer_class = IPDRegistrationSerializer
    
    def get_queryset(self):
        queryset = IPDRegistration.objects.all()
        ward_id = self.request.query_params.get('ward_id')
        if ward_id:
            queryset = queryset.filter(bed__ward_id=ward_id)
        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        ward_id = request.data.get('ward')
        bed_id = request.data.get('bed')
        # number = request.data.get('number') 
        # print(number)# Get the bed number directly
        patient_id = request.data.get('patient')

        if not bed_id or not ward_id or not patient_id:
            return Response({"message": "Bed number, ward ID, and patient ID are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bed = Bed.objects.get(id=bed_id)  # Query the bed directly using the number
        except Bed.DoesNotExist:
            raise Http404("Bed does not exist")

        ward = Ward.objects.get(pk=ward_id)

        if not ward:
            return Response({"message": "Ward does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        if IPDRegistration.objects.filter(patient_id=patient_id, ward_id=ward_id).exists():
            return Response({"message": "IPD registration with this bed already exists for the patient"}, status=status.HTTP_400_BAD_REQUEST)

        ipd_registration_data = {
            'patient': patient_id,
            'admission_date': request.data.get('admission_date'),
            'ward': ward_id,
            'bed': bed.id
        }

        ipd_registration_serializer = self.get_serializer(data=ipd_registration_data)
        ipd_registration_serializer.is_valid(raise_exception=True)
        self.perform_create(ipd_registration_serializer)

        bed.is_available = False
        bed.save()

        headers = self.get_success_headers(ipd_registration_serializer.data)
        return Response(ipd_registration_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class WardListCreateView(generics.ListCreateAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class WardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    
class IPDRegistrationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDRegistration.objects.all()
    serializer_class = IPDRegistrationSerializer

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        ward_id = request.data.get('ward')
        bed_id = request.data.get('bed')
        patient_id = request.data.get('patient')

        if not bed_id or not ward_id or not patient_id:
            return Response({"message": "Bed number, ward ID, and patient ID are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bed = Bed.objects.get(id=bed_id)
        except Bed.DoesNotExist:
            raise Http404("Bed does not exist")

        ward = Ward.objects.get(pk=ward_id)

        if not ward:
            return Response({"message": "Ward does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        if IPDRegistration.objects.filter(patient_id=patient_id, ward_id=ward_id).exclude(pk=instance.pk).exists():
            return Response({"message": "IPD registration with this bed already exists for the patient"}, status=status.HTTP_400_BAD_REQUEST)

        ipd_registration_data = {
            'patient': patient_id,
            'admission_date': request.data.get('admission_date'),
            'ward': ward_id,
            'bed': bed_id
        }

        ipd_registration_serializer = self.get_serializer(instance, data=ipd_registration_data)
        ipd_registration_serializer.is_valid(raise_exception=True)
        self.perform_update(ipd_registration_serializer)

        return Response(ipd_registration_serializer.data)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        bed = instance.bed
        if bed:
            bed.is_available = True
            bed.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class IPDDepositListCreateView(generics.ListCreateAPIView):
    queryset = IPDDeposit.objects.all()
    serializer_class = IPDDepositSerializer
    

class IPDDepositRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDeposit.objects.all()
    serializer_class = IPDDepositSerializer

class IPDDischargeListCreateView(generics.ListCreateAPIView):
    queryset = IPDDischarge.objects.all()
    serializer_class = IPDDischargeSerializer
    
    @transaction.atomic
    def post(self, request, format=None):
        admission_id = request.data.get('admission')
        discharge_date = request.data.get('discharge_date')
        
        if not admission_id or not discharge_date:
            return Response({"message": "Admission ID and discharge date are required"}, status=status.HTTP_400_BAD_REQUEST)

        ipd_registration = get_object_or_404(IPDRegistration, pk=admission_id)

        if ipd_registration.is_discharged:
            return Response({"message": "Patient is already discharged"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = IPDDischargeSerializer(data=request.data)
        if serializer.is_valid():
            # Create IPDDischarge instance
            discharge_instance = serializer.save(admission=ipd_registration, discharge_date=discharge_date)

            # Update IPDRegistration to mark patient as discharged
            ipd_registration.is_discharged = True
            ipd_registration.discharge_date = discharge_date
            ipd_registration.save()

            # Move patient details to discharge history
            DischargeHistory.objects.create(patient=ipd_registration.patient, discharge_date=discharge_date)

            # Delete the IPDRegistration instance
            ipd_registration.delete()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class IPDDischargeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDischarge.objects.all()
    serializer_class = IPDDischargeSerializer

class IPDAdmitReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDAdmitReport.objects.all()
    serializer_class = IPDAdmitReportSerializer

class IPDAdmitReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDAdmitReport.objects.all()
    serializer_class = IPDAdmitReportSerializer

class DischargeHistory(generics.ListCreateAPIView):
    queryset= DischargeHistory.objects.all()
    serializer_class = DischargeHistorySerializer

class IPDDepositReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDDepositReport.objects.all()
    serializer_class = IPDDepositReportSerializer

class IPDDepositReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDepositReport.objects.all()
    serializer_class = IPDDepositReportSerializer

from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from ipd.models.models import IPDDischarge, IPDRegistration, Bed

class IPDDischargeReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDDischargeReport.objects.all()
    serializer_class = IPDDischargeReportSerializer

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update the discharge date of the IPD registration
        admission = instance.admission
        ipd_registration = admission.ipd_registration
        ipd_registration.discharge_date = timezone.now()
        ipd_registration.is_discharged = True
        ipd_registration.save()

        return Response(serializer.data)


class IPDDischargeReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDischargeReport.objects.all()
    serializer_class = IPDDischargeReportSerializer

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update the discharge date of the IPD registration
        admission = instance.admission
        ipd_registration = admission.ipd_registration
        ipd_registration.discharge_date = timezone.now()
        ipd_registration.is_discharged = True
        ipd_registration.save()

        return Response(serializer.data)

class DepartmentReportListCreateView(generics.ListCreateAPIView):
    queryset = DepartmentReport.objects.all()
    serializer_class = DepartmentReportSerializer

class DepartmentReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentReport.objects.all()
    serializer_class = DepartmentReportSerializer

class WardWiseReportListCreateView(generics.ListCreateAPIView):
    queryset = WardWiseReport.objects.all()
    serializer_class = WardWiseReportSerializer

class WardWiseReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WardWiseReport.objects.all()
    serializer_class = WardWiseReportSerializer

class DoctorWiseReportListCreateView(generics.ListCreateAPIView):
    queryset = DoctorWiseReport.objects.all()
    serializer_class = DoctorWiseReportSerializer

class DoctorWiseReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorWiseReport.objects.all()
    serializer_class = DoctorWiseReportSerializer

class TPAReportListCreateView(generics.ListCreateAPIView):
    queryset = TPAReport.objects.all()
    serializer_class = TPAReportSerializer

class TPAReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TPAReport.objects.all()
    serializer_class = TPAReportSerializer

class BedListCreateView(generics.ListCreateAPIView):
    serializer_class = BedSerializer

    def get_queryset(self):
        queryset = Bed.objects.all()
        ward_id = self.request.query_params.get('ward_id')  # Get the ward ID from query params

        # If ward_id is provided, filter beds by that ward
        if ward_id:
            queryset = queryset.filter(ward_id=ward_id)

        return queryset

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        bed_number = request.data.get('bed')
        ward_id = request.data.get('ward')

        if not bed_number or not ward_id:
            return Response({"message": "Bed number and ward ID are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bed = Bed.get_available_bed(bed_number, ward_id)

            if bed is None:
                return Response({"message": "Selected bed is not available"}, status=status.HTTP_400_BAD_REQUEST)

        except Bed.DoesNotExist:
            return Response({"message": "Selected bed is not available"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the bed is already booked
        if BedBooking.objects.filter(bed=bed).exists():
            return Response({"message": "Selected bed is already booked"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the patient has already booked a bed
        if IPDRegistration.objects.filter(patient=request.data.get('patient')).exists():
            return Response({"message": "Patient already has a booked bed"}, status=status.HTTP_400_BAD_REQUEST)

        # Assuming you have the patient data available in the request data
        patient_data = {
            # Extract patient data from request
        }

        # Create IPDRegistration instance
        ipd_registration_serializer = IPDRegistrationSerializer(data=patient_data)
        if ipd_registration_serializer.is_valid():
            ipd_registration = ipd_registration_serializer.save()
        else:
            return Response(ipd_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Mark the bed as unavailable
        bed.is_available = False
        bed.save()

        # Create BedBooking instance
        BedBooking.objects.create(patient=ipd_registration.patient, bed=bed)

        # Return response
        return Response({"message": "Bed booked successfully"}, status=status.HTTP_201_CREATED)

class BedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class BedBookingListCreateView(generics.ListCreateAPIView):
    queryset = BedBooking.objects.all()
    serializer_class = BedBookingSerializer
    @transaction.atomic
    def update(self, request, *args, **kwargs):
        bed_instance = self.get_object()
        bed_number = request.data.get('number')
        ward_id = request.data.get('ward')

        if not bed_number or not ward_id:
            return Response({"message": "Bed number and ward ID are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bed = Bed.get_available_bed(bed_number, ward_id)

            if bed is None:
                return Response({"message": "Selected bed is not available"}, status=status.HTTP_400_BAD_REQUEST)

        except Bed.DoesNotExist:
            return Response({"message": "Selected bed is not available"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the bed is already booked
        if BedBooking.objects.filter(bed=bed).exists():
            return Response({"message": "Selected bed is already booked"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the patient has already booked a bed
        if IPDRegistration.objects.filter(patient=request.data.get('patient')).exists():
            return Response({"message": "Patient already has a booked bed"}, status=status.HTTP_400_BAD_REQUEST)

        # Assuming you have the patient data available in the request data
        patient_data = {
            # Extract patient data from request
        }

        # Create IPDRegistration instance
        ipd_registration_serializer = IPDRegistrationSerializer(data=patient_data)
        if ipd_registration_serializer.is_valid():
            ipd_registration = ipd_registration_serializer.save()
        else:
            return Response(ipd_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Mark the bed as unavailable
        bed.is_available = False
        bed.save()

        # Create BedBooking instance
        BedBooking.objects.create(patient=ipd_registration.patient, bed=bed)

        # Return response
        return Response({"message": "Bed updated and booked successfully"}, status=status.HTTP_200_OK)

class BedBookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedBooking.objects.all()
    serializer_class = BedBookingSerializer

class BedAllocationListCreateView(generics.ListCreateAPIView):
    queryset = BedAllocation.objects.all()
    serializer_class = BedAllocationSerializer

class BedAllocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedAllocation.objects.all()
    serializer_class = BedAllocationSerializer

class BedStatusUpdateListCreateView(generics.ListCreateAPIView):
    queryset = BedStatusUpdate.objects.all()
    serializer_class = BedStatusUpdateSerializer

class BedStatusUpdateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedStatusUpdate.objects.all()
    serializer_class = BedStatusUpdateSerializer

class BedAvailabilityListCreateView(generics.ListCreateAPIView):
    queryset = BedAvailability.objects.all()
    serializer_class = BedAvailabilitySerializer

class BedAvailabilityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedAvailability.objects.all()
    serializer_class = BedAvailabilitySerializer
 