from django.db import models
from doctor.models.models import Doctor
from patient.models.models import Patient
from hos_login.models import Custom_User
TIME_SLOTS = [
    ('9:30-9:40', '9:30 AM - 9:40 AM'),
    ('9:40-9:50', '9:40 AM - 9:50 AM'),
    ('9:50-10:00', '9:50 AM - 10:00 AM'),
    ('10:00-10:10', '10:00 AM - 10:10 AM'),
    ('10:10-10:20', '10:10 AM - 10:20 AM'),
    ('10:20-10:30', '10:20 AM - 10:30 AM'),
    ('10:30-10:40', '10:30 AM - 10:40 AM'),
    ('10:40-10:50', '10:40 AM - 10:50 AM'),
    ('10:50-11:00', '10:50 AM - 11:00 AM'),
    ('11:00-11:10', '11:00 AM - 11:10 AM'),
    ('11:10-11:20', '11:10 AM - 11:20 AM'),
    ('11:20-11:30', '11:20 AM - 11:30 AM'),
    ('11:30-11:40', '11:30 AM - 11:40 AM'),
    ('11:40-11:50', '11:40 AM - 11:50 AM'),
    ('11:50-12:00', '11:50 AM - 12:00 PM'),
    ('12:00-12:10', '12:00 PM - 12:10 PM'),
    ('12:10-12:20', '12:10 PM - 12:20 PM'),
    ('12:20-12:30', '12:20 PM - 12:30 PM'),
    ('12:30-12:40', '12:30 PM - 12:40 PM'),
    ('12:40-12:50', '12:40 PM - 12:50 PM'),
    ('12:50-1:00', '12:50 PM - 1:00 PM'),
    ('18:00-18:10', '6:00 PM - 6:10 PM'),
    ('18:10-18:20', '6:10 PM - 6:20 PM'),
    ('18:20-18:30', '6:20 PM - 6:30 PM'),
    ('18:30-18:40', '6:30 PM - 6:40 PM'),
    ('18:40-18:50', '6:40 PM - 6:50 PM'),
    ('18:50-19:00', '6:50 PM - 7:00 PM'),
    ('19:00-19:10', '7:00 PM - 7:10 PM'),
    ('19:10-19:20', '7:10 PM - 7:20 PM'),
    ('19:20-19:30', '7:20 PM - 7:30 PM'),
    ('19:30-19:40', '7:30 PM - 7:40 PM'),
    ('19:40-19:50', '7:40 PM - 7:50 PM'),
    ('19:50-20:00', '7:50 PM - 8:00 PM'),
    ('20:00-20:10', '8:00 PM - 8:10 PM'),
    ('20:10-20:20', '8:10 PM - 8:20 PM'),
    ('20:20-20:30', '8:20 PM - 8:30 PM'),
    ('20:30-20:40', '8:30 PM - 8:40 PM'),
    ('20:40-20:50', '8:40 PM - 8:50 PM'),
    ('20:50-21:00', '8:50 PM - 9:00 PM'),
    ('21:00-21:10', '9:00 PM - 9:10 PM'),
    ('21:10-21:20', '9:10 PM - 9:20 PM'),
    ('21:20-21:30', '9:20 PM - 9:30 PM'),
    ('21:30-21:40', '9:30 PM - 9:40 PM'),
    ('21:40-21:50', '9:40 PM - 9:50 PM'),
    ('21:50-22:00', '9:50 PM - 10:00 PM'),
    ('22:00-22:10', '10:00 PM - 10:10 PM'),
    ('22:10-22:20', '10:10 PM - 10:20 PM'),
    ('22:20-22:30', '10:20 PM - 10:30 PM'),
]

status_choices = [
    ('pending', 'Pending'),
    ('booked', 'Booked'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
    # Add more status choices as needed
]

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey( Patient , on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   # clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    owner= models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)
  #  date = models.DateField()
    time_slot = models.DateTimeField(default=None)
    status = models.CharField(max_length=20, choices=status_choices, default='available')