from django.db import models

from django.db import models

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
   
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    facility_code = models.CharField(max_length=100, blank=True)
    membernum = models.CharField(max_length=100, blank=True)
    Insurance_name = models.CharField(max_length=100, blank=True)
    card_num = models.CharField(max_length=100, blank=True)
    Insurance_Provider = models.CharField(max_length=100, blank=True)   
    Gender = models.CharField(max_length=10)  
    DOB = models.DateField()
    PinCode = models.CharField(max_length=10, blank=True, null=True) 
    def __str__(self):
        return f"{self.fullname} - Admission ID: {self.PatientID} "

class PatientHistory(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    MedicalHistoryDetails = models.TextField()
    TreatmentDetails = models.TextField()

class PatientBilling(models.Model):
    BillingID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    InvoiceDetails = models.TextField()

class PatientLedger(models.Model):
    LedgerID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TransactionDetails = models.TextField()

class TreatmentInformation(models.Model):
    TreatmentID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TreatmentDetails = models.TextField()

class PatientReminder(models.Model):
    ReminderID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ReminderDetails = models.TextField()

class PatientVisitList(models.Model):
    VisitID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    VisitDate = models.DateField()
    Reason = models.TextField()