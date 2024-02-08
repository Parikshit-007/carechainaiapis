from django.db import models
from patient.models.models import Patient
from django.db.models.signals import post_save
from django.dispatch import receiver
class Ward(models.Model):
    name = models.CharField(max_length=50)
    total_beds = models.PositiveIntegerField(default=0)  # Total number of beds for the ward

    def __str__(self):
        return f"{self.name}"

class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    @receiver(post_save, sender=Ward)
    def create_beds(sender, instance, created, **kwargs):
       if created:
          total_beds = instance.total_beds
          for bed_number in range(1, total_beds + 1):
             Bed.objects.create(ward=instance, number=str(bed_number))
    def is_available_in_ward(self, ward):
        return self.ward == ward and self.is_available         
    def __str__(self):
        return f"Ward Name: {self.ward.name} Bed No:{self.number}"
class IPDRegistration(models.Model):

    admission_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE, default= None)
    def __str__(self):
        return f"{self.patient.fullname} - Admission ID: {self.patient.PatientID}"   
 
class BedBooking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)

class BedAllocation(models.Model):
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)

class BedStatusUpdate(models.Model):
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    updated_status = models.BooleanField()
    update_date = models.DateField(auto_now_add=True)

class WardWiseBedReport(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    occupied_beds = models.IntegerField()
    available_beds = models.IntegerField()
    report_date = models.DateField(auto_now_add=True)

class IPDDeposit(models.Model):
    deposit_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_date = models.DateField()
    def __str__(self):
        return f"{self.deposit_id} - {self.admission.patient.FirstName} {self.admission.patient.LastName}"

class IPDDischarge(models.Model):
    discharge_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    discharge_date = models.DateField()
    discharge_summary = models.TextField()

class IPDAdmitReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    report_details = models.TextField()

class IPDDepositReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    deposit = models.ForeignKey(IPDDeposit, on_delete=models.CASCADE)
    report_details = models.TextField()

class IPDDischargeReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    discharge = models.ForeignKey(IPDDischarge, on_delete=models.CASCADE)
    report_details = models.TextField()

class DepartmentReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50)
    data_details = models.TextField()

class WardWiseReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    ward = models.CharField(max_length=50)
    data_details = models.TextField()

class DoctorWiseReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    doctor_id = models.CharField(max_length=20)
    data_details = models.TextField()

class TPAReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    tpa_id = models.CharField(max_length=20)
    transaction_details = models.TextField()

class BedAvailability(models.Model):
    bed = models.OneToOneField(Bed, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)
