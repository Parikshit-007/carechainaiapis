from django.db import models
from hos_login.models import Custom_User
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    RELATION_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Spouse', 'Spouse'),
        ('Friend', 'Friend'),
        ('Other', 'Other'),
    ]

    PatientID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    Relationship = models.CharField(max_length=100, blank=True)
    fullname = models.CharField(max_length=255, blank=True)
    Gender = models.CharField(max_length=10, blank=True)
    blood = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=20, blank=True)
    referred = models.CharField(max_length=255, blank=True)
    allergy = models.TextField(blank=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE) 
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    facility_code = models.CharField(max_length=100, blank=True)
    membernum = models.CharField(max_length=100, blank=True)
    Insurance_name = models.CharField(max_length=100, blank=True)
    card_num = models.CharField(max_length=100, blank=True)
    Insurance_Provider = models.CharField(max_length=100, blank=True)   
    Gender = models.CharField(max_length=10)  
    DOB = models.DateField()
    Register_Date = models.DateField()

    PinCode = models.CharField(max_length=10, blank=True, null=True) 
    #Register_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.fullname} - Admission ID: {self.PatientID} "

    def save(self, *args, **kwargs):
        if not self.PatientID:
            max_id = Patient.objects.aggregate(models.Max('PatientID'))['PatientID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.PatientID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)

class PatientHistory(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    MedicalHistoryDetails = models.TextField()
    TreatmentDetails = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=False) 

    def save(self, *args, **kwargs):
        if not self.HistoryID:
            max_id = PatientHistory.objects.aggregate(models.Max('HistoryID'))['HistoryID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.HistoryID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)

class PatientBilling(models.Model):
    BillingID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    InvoiceDetails = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=False) 

    def save(self, *args, **kwargs):
        if not self.BillingID:
            max_id = PatientBilling.objects.aggregate(models.Max('BillingID'))['BillingID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.BillingID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)

class PatientLedger(models.Model):
    LedgerID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TransactionDetails = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=False) 

    def save(self, *args, **kwargs):
        if not self.LedgerID:
            max_id = PatientLedger.objects.aggregate(models.Max('LedgerID'))['LedgerID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.LedgerID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)

class TreatmentInformation(models.Model):
    TreatmentID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TreatmentDetails = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=False) 

    def save(self, *args, **kwargs):
        if not self.TreatmentID:
            max_id = TreatmentInformation.objects.aggregate(models.Max('TreatmentID'))['TreatmentID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.TreatmentID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)

class PatientReminder(models.Model):
    ReminderID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ReminderDetails = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=False) 

    def save(self, *args, **kwargs):
        if not self.ReminderID:
            max_id = PatientReminder.objects.aggregate(models.Max('ReminderID'))['ReminderID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.ReminderID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)

class PatientVisitList(models.Model):
    VisitID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    VisitDate = models.DateField()
    Reason = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=False) 

    def save(self, *args, **kwargs):
        if not self.VisitID:
            max_id = PatientVisitList.objects.aggregate(models.Max('VisitID'))['VisitID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.VisitID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)
