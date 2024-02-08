from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
      #  ('Other', 'Other'),
    ]
    DoctorID = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    dob = models.DateField()
    specialty = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Address = models.TextField()
    PinCode = models.CharField(max_length=10, blank=True, null=True)
    experince = models.CharField(max_length=100)
    education_qualification= models.CharField(max_length =100)
    working_details= models.CharField(max_length =100)
    identity_proof=models.FileField(upload_to='identity_proofs/')
    medical_liscence=  models.FileField(upload_to='medical_licenses/')

