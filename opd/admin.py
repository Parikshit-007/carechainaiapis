from django.contrib import admin

# Register your models here.
# admin.py in OPD app
from django.contrib import admin
from opd.models.models import OPD_REGISTER, OPD_Billing, OPD_REPORT, OPD_PRESCRIPTION, OPDTOIPDTRANSFER, OPDPatientSummary, Depwisereport, RefDoctorReport, ConsultantDoctorReport

@admin.register(OPD_REGISTER)
class OPD_REGISTERAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'patient_id', 'visit_date', 'doctor_id', 'department')

@admin.register(OPD_Billing)
class OPD_BillingAdmin(admin.ModelAdmin):
    list_display = ('billing_id', 'visit_id', 'invoice_detail')

@admin.register(OPD_REPORT)
class OPD_REPORTAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'visit_id', 'report_details')

# Repeat for the remaining models...
