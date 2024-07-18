from django.db import models

# Create your models here.
from hos_login.models import Custom_User

# Create your models here.
class Hospital(models.Model):
    name=models.CharField(max_length=50, default=None)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='logos/')
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    gstin = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=50)
    def __str__(self):
      return self.name
