
from django.db import models
from django.contrib.auth.models import User

class StaffAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    is_present = models.BooleanField(default=True)

class StaffShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift_start = models.DateTimeField()
    shift_end = models.DateTimeField()

class StaffLeave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_start = models.DateField()
    leave_end = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)

class StaffPerformance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation_date = models.DateField()
    performance_rating = models.IntegerField()
