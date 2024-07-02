from django.db import models
from django.contrib.auth.models import User
from hos_login.models import Custom_User
class Staff(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE ,default=None)
   # owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
  #  owwner = models.ForeignKey(Custom_User, on_delete=models.CASCADE, default=None)
#    op= models.ForeignKey(Custom_User , on_delete=models.CASCADE, default=None)
    owner= models.ForeignKey(Custom_User , on_delete=models.CASCADE , default=None)
   # owwner= models.ForeignKey(Custom_User , on_delete=models.CASCADE , default=None)
    name = models.CharField(max_length=100)
    #gender = models.TextField(max_length=10)
    # phone_number = models.CharField(max_length=15,default=None,null=False)
    address = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=100 ,default=None)
    #phone_number = models.CharField()
   # date_of_birth = models.DateField( default=None)
    dob =models.DateField(default=None,null = True,blank = True)
   # hire_date = models.DateField(default=None)
    hire_datee =models.DateField(default=None,null = True,blank = True)
    department = models.CharField(max_length=100)
    phone_number =models.CharField(max_length=15,default=None,null = True,blank = True)

class StaffAttendance(models.Model):
   # owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    is_present = models.BooleanField(default=True)
    Staff= models.ForeignKey(Staff, on_delete=models.CASCADE , default= None)

class StaffShift(models.Model):
    #owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Custom_User , on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.DateTimeField()
    Staff= models.ForeignKey(Staff, on_delete=models.CASCADE , default= None)

class StaffLeave(models.Model):
    #owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    owner=models.ForeignKey(Custom_User , on_delete=models.CASCADE)
    leave_start = models.DateField()
    leave_end = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)
    Staff= models.ForeignKey(Staff, on_delete=models.CASCADE , default= None)

class StaffPerformance(models.Model):
   # owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Custom_User , on_delete=models.CASCADE)
    evaluation_date = models.DateField()
    performance_rating = models.IntegerField()
    Staff= models.ForeignKey(Staff, on_delete=models.CASCADE , default= None)
