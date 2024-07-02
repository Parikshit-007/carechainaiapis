from django.db import models

from hos_login.models import Custom_User
#from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
      #  ('Other', 'Other'),
    ]
    DoctorID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)
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
    def save(self, *args, **kwargs):
        if not self.DoctorID:
            max_id = Doctor.objects.aggregate(models.Max('DoctorID'))['DoctorID__max'] or 0
            owner_id = self.owner.pk if self.owner else 0
            self.DoctorID = (owner_id * 1000) + max_id + 1
        super().save(*args, **kwargs)
