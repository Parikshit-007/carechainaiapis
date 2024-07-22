# models.py
from django.db import models
from patient.models.models import Patient
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db import transaction
from hos_login.models import Custom_User

class BedManager(models.Manager):
    def bed_set(self, number, is_available=True):
        return self.get(number=number, is_available=bool(is_available))

class Ward(models.Model):
    name = models.CharField(max_length=50)
    daily_charge = models.PositiveIntegerField(default=0)
    total_beds = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.name}"

class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None)

    objects = BedManager()

    def __str__(self):
        return f"Ward Name: {self.ward.name} Bed No: {self.number}"

class IPDRegistration(models.Model):
    admission_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    bed = models.OneToOneField(Bed, on_delete=models.CASCADE)
    discharge_date = models.DateField(null=True, blank=True)
    is_discharged = models.BooleanField(default=False)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.patient.fullname} - Admission ID: {self.patient.PatientID}"

    def calculate_total_charges(self):
        if self.admission_date and self.discharge_date:
            duration = self.discharge_date - self.admission_date
            total_days = duration.days + 1
            total_charges = total_days * self.ward.daily_charge
            return total_charges
        return 0

class DischargeHistory(models.Model):
    admission_date = models.DateField(default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"{self.patient.fullname} - Discharge Date: {self.discharge_date}"

    def calculate_total_charges(self):
        if self.admission_date and self.discharge_date:
            duration = self.discharge_date - self.admission_date
            total_days = duration.days + 1
            ward_daily_charge = self.patient.ipdregistration_set.first().ward.daily_charge
            total_charges = total_days * ward_daily_charge
            return total_charges
        return 0

class IPDDischarge(models.Model):
    discharge_id = models.AutoField(primary_key=True)
    admission = models.OneToOneField(IPDRegistration, on_delete=models.CASCADE)
    discharge_date = models.DateField(null=True, blank=True)
    admission_date = models.DateField(default=None)
    discharge_summary = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None, null=True)

class BedBooking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None)

@receiver(post_save, sender=Ward)
def create_beds(sender, instance, created, **kwargs):
    if created:
        total_beds = instance.total_beds
        beds_to_create = []
        for bed_number in range(1, total_beds + 1):
            beds_to_create.append(Bed(ward=instance, number=str(bed_number), is_available=True, owner=instance.owner))
        Bed.objects.bulk_create(beds_to_create)

@receiver(post_save, sender=Ward)
def update_beds(sender, instance, created, **kwargs):
    if not created:
        total_beds = instance.total_beds
        current_beds_count = instance.bed_set.count()

        if current_beds_count < total_beds:
            beds_to_create = []
            for bed_number in range(current_beds_count + 1, total_beds + 1):
                beds_to_create.append(Bed(ward=instance, number=str(bed_number), is_available=True, owner=instance.owner))
            Bed.objects.bulk_create(beds_to_create)
        elif current_beds_count > total_beds:
            beds_to_delete = instance.bed_set.order_by('-number')[:current_beds_count - total_beds]
            for bed in beds_to_delete:
                bed.delete()

@receiver(post_save, sender=IPDRegistration)
def update_bed_availability(sender, instance, created, **kwargs):
    if created:
        bed = instance.bed
        bed.is_available = False
        bed.save()

@receiver(post_save, sender=IPDDischarge)
def move_to_discharge_history(sender, instance, created, **kwargs):
    if created:
        discharged_patient = instance.admission.patient
        DischargeHistory.objects.create(patient=discharged_patient, discharge_date=instance.discharge_date, owner=instance.owner, admission_date=instance.admission_date)

        admission = instance.admission
        admission.is_discharged = True
        admission.discharge_date = instance.discharge_date
        admission.save()

        bed = admission.bed
        if bed:
            bed.is_available = True
            bed.save()

        admission.delete()

@receiver(pre_delete, sender=IPDRegistration)
def delete_bed_availability(sender, instance, **kwargs):
    bed = instance.bed
    if bed:
        bed.is_available = True
        bed.save()
# @receiver(pre_delete, sender=IPDRegistration)
# def handle_discharge(sender, instance, **kwargs):
#     if instance.is_discharged:
#         # Create IPDDischarge instance
#         discharge_instance, created = IPDDischarge.objects.get_or_create(admission=instance)
#         discharge_instance.discharge_date = instance.discharge_date
#       # discharge_instance.ward= instance.ward
#         # ward=instance.ward
#         discharge_instance.admission_date= instance.admission_date
#         discharge_instance.save()
        
#         # Move patient details to discharge history
#         DischargeHistory.objects.create(patient=instance.patient, admission_date=instance.admission_date,discharge_date=instance.discharge_date)

        # Mark the bed as available again
        # bed = instance.bed
        # if bed:
        #     bed.is_available = True
        #     bed.save()
        # # instance.delete()    

        # # Delete the IPDRegistration instance and cascade delete related objects
        # with transaction.atomic():
        #     # Delete related objects first to avoid integrity errors
        #     instance.bed = None
        #     instance.save()
        #     instance.patient.delete()
        #     instance.save()
class DischargeHistory(models.Model):
    # addmission_date = models.DateField(default=None) 
    #ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    admission_date= models.DateField(default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None,null=True)
    def __str__(self):
        return f"{self.patient.fullname} - Discharge Date: {self.discharge_date}"
    def calculate_total_charges(self):
        if self.addmission_date and self.discharge_date:
            duration = self.discharge_date - self.addmission_date
            total_days = duration.days + 1
            ward_daily_charge = self.patient.ipdregistration_set.first().ward.daily_charge
            total_charges = total_days * ward_daily_charge
            return total_charges
        return 0
    
    def _str_(self):
        return f"{self.patient.fullname} - Discharge Date: {self.discharge_date}"

class IPDDischarge(models.Model):
    discharge_id = models.AutoField(primary_key=True)
    admission = models.OneToOneField(IPDRegistration, on_delete=models.CASCADE)
    discharge_date = models.DateField(null=True, blank=True)
    admission_date = models.DateField(default=None) 
    discharge_summary = models.TextField()
    #ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None,null=True) 
@receiver(post_save, sender=IPDDischarge)
def move_to_discharge_history(sender, instance, created, **kwargs):
    if created:
        discharged_patient = instance.admission.patient
        # Create a record in the discharge history
        DischargeHistory.objects.create(patient=discharged_patient, discharge_date=instance.discharge_date, owner=instance.owner, admission_date=instance.admission_date)

        # Update the IPDRegistration instance to mark it as discharged
        admission = instance.admission
        #ward = instance.ward
        admission_date = instance.admission_date,  # Add admission_date here
        admission.is_discharged = True
        admission.discharge_date = instance.discharge_date
        admission.save()

        # Mark the bed as available again (assuming one-to-one relationship)
        bed = admission.bed
        if bed:
            bed.is_available = True
            bed.save()

        # Delete the IPDRegistration instance
        admission.delete()


class BedBooking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class BedAllocation(models.Model):
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class BedStatusUpdate(models.Model):
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    updated_status = models.BooleanField()
    update_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class WardWiseBedReport(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE,default=None)
    occupied_beds = models.IntegerField()
    available_beds = models.IntegerField()
    report_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class IPDDeposit(models.Model):
    deposit_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_date = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

    def __str__(self):
        return f"{self.deposit_id} - {self.admission.patient.FirstName} {self.admission.patient.LastName}"

# class IPDDischarge(models.Model):
#     discharge_id = models.AutoField(primary_key=True)
#     admission = models.OneToOneField(IPDRegistration, on_delete=models.CASCADE)
#     discharge_date = models.DateField()
#     discharge_summary = models.TextField()
# @receiver(post_save, sender=IPDDischarge)
# def move_to_discharge_history(sender, instance, created, **kwargs):
#     if created:
#         discharged_patient = instance.admission.patient
#         # Create a record in the discharge history
#         DischargeHistory.objects.create(patient=discharged_patient, discharge_date=instance.discharge_date)
#         # Mark the bed as available again
#         bed = instance.admission.bed
#         bed.is_available = True
#         bed.save()

#         # Update the IPDRegistration instance to mark it as discharged
#         admission = instance.admission
#         admission.is_discharged = True
#         admission.save()
class IPDAdmitReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    report_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class IPDDepositReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    deposit = models.ForeignKey(IPDDeposit, on_delete=models.CASCADE)
    report_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class IPDDischargeReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    discharge = models.ForeignKey(IPDDischarge, on_delete=models.CASCADE)
    report_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class DepartmentReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50)
    data_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class WardWiseReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    ward = models.CharField(max_length=50)
    data_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class DoctorWiseReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    doctor_id = models.CharField(max_length=20)
    data_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class TPAReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    tpa_id = models.CharField(max_length=20)
    transaction_details = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 

class BedAvailability(models.Model):
    bed = models.OneToOneField(Bed, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None) 
