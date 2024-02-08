from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hospital, User

admin.site.register(Hospital)
admin.site.register(User)
