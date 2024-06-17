from django.db import models
from patient.models.models import Patient
from doctor.models.models import Doctor
from hos_login.models import Custom_User

class OPD_REGISTER(models.Model):
    visit_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateField(auto_now_add=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class OPD_Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    visit_id = models.ForeignKey(OPD_REGISTER, on_delete=models.CASCADE)
    invoice_detail = models.TextField(default=None)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class OPD_REPORT(models.Model):
    report_id = models.AutoField(primary_key=True)
    visit_id = models.ForeignKey(OPD_REGISTER, on_delete=models.CASCADE)
    report_details = models.TextField(blank=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class OPD_PRESCRIPTION(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    visit_id = models.ForeignKey(OPD_REGISTER, on_delete=models.CASCADE)
    prescription_details = models.TextField(blank=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class OPDTOIPDTRANSFER(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    visit_id = models.ForeignKey(OPD_REGISTER, on_delete=models.CASCADE)
    ipd_admission_id = models.TextField(blank=False)
    admission_date = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class OPDPatientSummary(models.Model):
    summary_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    summary_details = models.TextField(blank=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class Depwisereport(models.Model):
    report_id = models.AutoField(primary_key=True)
    department = models.TextField(blank=False)
    date_details = models.DateField(default=None)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class RefDoctorReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    ref_doc_id = models.TextField(blank=False)
    referrals_details = models.TextField(blank=False)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class ConsultantDoctorReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    consultant_doctor_id = models.TextField(blank=False)
    performance_details = models.TextField(blank=False)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)
