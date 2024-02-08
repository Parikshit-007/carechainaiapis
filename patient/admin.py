# admin.py

from django.contrib import admin
from patient.models.models import Patient, PatientHistory, PatientBilling, PatientLedger, TreatmentInformation, PatientReminder, PatientVisitList

# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ['PatientID', 'FirstName', 'MiddleName', 'LastName', 'Gender', 'DOB', 'ContactNumber']
#     search_fields = ['FirstName', 'LastName', 'ContactNumber']
#     list_filter = ['Gender']
    # Add more customization options as needed

@admin.register(PatientHistory)
class PatientHistoryAdmin(admin.ModelAdmin):
    list_display = ['HistoryID', 'PatientID', 'MedicalHistoryDetails', 'TreatmentDetails']
    search_fields = ['PatientID__FirstName', 'PatientID__LastName']
    # Add more customization options as needed

@admin.register(PatientBilling)
class PatientBillingAdmin(admin.ModelAdmin):
    list_display = ['BillingID', 'PatientID', 'InvoiceDetails']
    search_fields = ['PatientID__FirstName', 'PatientID__LastName']
    # Add more customization options as needed

@admin.register(PatientLedger)
class PatientLedgerAdmin(admin.ModelAdmin):
    list_display = ['LedgerID', 'PatientID', 'TransactionDetails']
    search_fields = ['PatientID__FirstName', 'PatientID__LastName']
    # Add more customization options as needed

@admin.register(TreatmentInformation)
class TreatmentInformationAdmin(admin.ModelAdmin):
    list_display = ['TreatmentID', 'PatientID', 'TreatmentDetails']
    search_fields = ['PatientID__FirstName', 'PatientID__LastName']
    # Add more customization options as needed

@admin.register(PatientReminder)
class PatientReminderAdmin(admin.ModelAdmin):
    list_display = ['ReminderID', 'PatientID', 'ReminderDetails']
    search_fields = ['PatientID__FirstName', 'PatientID__LastName']
    # Add more customization options as needed

@admin.register(PatientVisitList)
class PatientVisitListAdmin(admin.ModelAdmin):
    list_display = ['VisitID', 'PatientID', 'VisitDate', 'Reason']
    search_fields = ['PatientID__FirstName', 'PatientID__LastName']
    list_filter = ['VisitDate']
    # Add more customization options as needed
