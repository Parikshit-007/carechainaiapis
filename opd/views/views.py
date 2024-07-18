from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from opd.models.models import (
    OPD_REGISTER,
    OPD_Billing,
    OPD_REPORT,
    OPD_PRESCRIPTION,
    OPDTOIPDTRANSFER,
    OPDPatientSummary,
    Depwisereport,
    RefDoctorReport,
    ConsultantDoctorReport,
)
from opd.serializers import (
    OPD_REGISTERSerializer,
    OPD_BillingSerializer,
    OPD_REPORTSerializer,
    OPD_PRESCRIPTIONSerializer,
    OPDTOIPDTRANSFERSerializer,
    OPDPatientSummarySerializer,
    DepwisereportSerializer,
    RefDoctorReportSerializer,
    ConsultantDoctorReportSerializer,
)

class OPD_REGISTERViewSet(viewsets.ModelViewSet):
   
    serializer_class = OPD_REGISTERSerializer
    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = OPD_REGISTER.objects.filter(owner=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPD_BillingViewSet(viewsets.ModelViewSet):
    #queryset = OPD_Billing.objects.all()
    serializer_class = OPD_BillingSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = OPD_Billing.objects.filter(owner=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPD_REPORTViewSet(viewsets.ModelViewSet):
   # queryset = OPD_REPORT.objects.all()
    serializer_class = OPD_REPORTSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = OPD_REPORT.objects.filter(owner=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPD_PRESCRIPTIONViewSet(viewsets.ModelViewSet):
   # queryset = OPD_PRESCRIPTION.objects.all()
    serializer_class = OPD_PRESCRIPTIONSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = OPD_PRESCRIPTION.objects.filter(owner=self.request.user)

        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPDTOIPDTRANSFERViewSet(viewsets.ModelViewSet):
  #  queryset = OPDTOIPDTRANSFER.objects.all()
    serializer_class = OPDTOIPDTRANSFERSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = OPDTOIPDTRANSFER.objects.filter(owner=self.request.user)

        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPDPatientSummaryViewSet(viewsets.ModelViewSet):
   # queryset = OPDPatientSummary.objects.all()
    serializer_class = OPDPatientSummarySerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = OPDPatientSummary.objects.filter(owner=self.request.user)

        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DepwisereportViewSet(viewsets.ModelViewSet):
   # queryset = Depwisereport.objects.all()
    serializer_class = DepwisereportSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = Depwisereport.objects.filter(owner=self.request.user)

        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RefDoctorReportViewSet(viewsets.ModelViewSet):
    #queryset = RefDoctorReport.objects.all()
    serializer_class = RefDoctorReportSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = RefDoctorReport.objects.filter(owner=self.request.user)

        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ConsultantDoctorReportViewSet(viewsets.ModelViewSet):
  #  queryset = ConsultantDoctorReport.objects.all()
    serializer_class = ConsultantDoctorReportSerializer

    def get_queryset(self):
        # Ensure user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this data.")

        # Get the list of patients owned by the current user
        queryset = ConsultantDoctorReport.objects.filter(owner=self.request.user)

        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)