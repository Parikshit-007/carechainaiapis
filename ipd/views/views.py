# ipd/views.py
from rest_framework import generics
from ipd.models.models import (
    BedAllocation, BedAvailability, BedBooking, BedStatusUpdate, IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport, 
    IPDDepositReport, IPDDischargeReport, DepartmentReport, Ward, 
    WardWiseReport, DoctorWiseReport, TPAReport, Bed
)
from ipd.serializers import (
    IPDRegistrationSerializer, IPDDepositSerializer, IPDDischargeSerializer, 
    IPDAdmitReportSerializer, IPDDepositReportSerializer, IPDDischargeReportSerializer,
    DepartmentReportSerializer, WardSerializer, WardWiseReportSerializer, DoctorWiseReportSerializer, TPAReportSerializer , BedSerializer, BedBookingSerializer, BedAllocationSerializer, \
    BedStatusUpdateSerializer, BedAvailabilitySerializer
)

class IPDRegistrationListCreateView(generics.ListCreateAPIView):
    queryset = IPDRegistration.objects.all()
    serializer_class = IPDRegistrationSerializer
    def get_queryset(self):
      qs= IPDRegistration.objects.all()
      title = self.request.query_params.get('title')
      if title is not None:
         qs= qs.filter(title__icontains=title)
      return qs    
    
class WardListCreateView(generics.ListCreateAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class WardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    
class IPDRegistrationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDRegistration.objects.all()
    serializer_class = IPDRegistrationSerializer

class IPDDepositListCreateView(generics.ListCreateAPIView):
    queryset = IPDDeposit.objects.all()
    serializer_class = IPDDepositSerializer

class IPDDepositRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDeposit.objects.all()
    serializer_class = IPDDepositSerializer

class IPDDischargeListCreateView(generics.ListCreateAPIView):
    queryset = IPDDischarge.objects.all()
    serializer_class = IPDDischargeSerializer

class IPDDischargeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDischarge.objects.all()
    serializer_class = IPDDischargeSerializer

class IPDAdmitReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDAdmitReport.objects.all()
    serializer_class = IPDAdmitReportSerializer

class IPDAdmitReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDAdmitReport.objects.all()
    serializer_class = IPDAdmitReportSerializer

class IPDDepositReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDDepositReport.objects.all()
    serializer_class = IPDDepositReportSerializer

class IPDDepositReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDepositReport.objects.all()
    serializer_class = IPDDepositReportSerializer

class IPDDischargeReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDDischargeReport.objects.all()
    serializer_class = IPDDischargeReportSerializer

class IPDDischargeReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDischargeReport.objects.all()
    serializer_class = IPDDischargeReportSerializer

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
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class BedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class BedBookingListCreateView(generics.ListCreateAPIView):
    queryset = BedBooking.objects.all()
    serializer_class = BedBookingSerializer

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