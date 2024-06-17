from rest_framework import viewsets
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
    queryset = OPD_REGISTER.objects.all()
    serializer_class = OPD_REGISTERSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPD_BillingViewSet(viewsets.ModelViewSet):
    queryset = OPD_Billing.objects.all()
    serializer_class = OPD_BillingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPD_REPORTViewSet(viewsets.ModelViewSet):
    queryset = OPD_REPORT.objects.all()
    serializer_class = OPD_REPORTSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPD_PRESCRIPTIONViewSet(viewsets.ModelViewSet):
    queryset = OPD_PRESCRIPTION.objects.all()
    serializer_class = OPD_PRESCRIPTIONSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPDTOIPDTRANSFERViewSet(viewsets.ModelViewSet):
    queryset = OPDTOIPDTRANSFER.objects.all()
    serializer_class = OPDTOIPDTRANSFERSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OPDPatientSummaryViewSet(viewsets.ModelViewSet):
    queryset = OPDPatientSummary.objects.all()
    serializer_class = OPDPatientSummarySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DepwisereportViewSet(viewsets.ModelViewSet):
    queryset = Depwisereport.objects.all()
    serializer_class = DepwisereportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RefDoctorReportViewSet(viewsets.ModelViewSet):
    queryset = RefDoctorReport.objects.all()
    serializer_class = RefDoctorReportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ConsultantDoctorReportViewSet(viewsets.ModelViewSet):
    queryset = ConsultantDoctorReport.objects.all()
    serializer_class = ConsultantDoctorReportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
