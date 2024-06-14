
from django.contrib import admin
from ipd.models.models import (
    IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport,
    IPDDepositReport, IPDDischargeReport, DepartmentReport,
    WardWiseReport, DoctorWiseReport, TPAReport
)

# Register your models with the admin site

@admin.register(IPDRegistration)
class IPDRegistrationAdmin(admin.ModelAdmin):
    list_display = ('admission_id', 'patient', 'admission_date', 'ward', 'bed')

@admin.register(IPDDeposit)
class IPDDepositAdmin(admin.ModelAdmin):
    list_display = ('deposit_id', 'admission', 'deposit_amount', 'deposit_date')

@admin.register(IPDDischarge)
class IPDDischargeAdmin(admin.ModelAdmin):
    list_display = ('discharge_id', 'admission', 'discharge_date', 'discharge_summary')

@admin.register(IPDAdmitReport)
class IPDAdmitReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'admission', 'report_details')

@admin.register(IPDDepositReport)
class IPDDepositReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'deposit', 'report_details')

@admin.register(IPDDischargeReport)
class IPDDischargeReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'discharge', 'report_details')

@admin.register(DepartmentReport)
class DepartmentReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'department', 'data_details')

@admin.register(WardWiseReport)
class WardWiseReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'ward', 'data_details')

@admin.register(DoctorWiseReport)
class DoctorWiseReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'doctor_id', 'data_details')

@admin.register(TPAReport)
class TPAReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'tpa_id', 'transaction_details')
