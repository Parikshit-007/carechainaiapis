# models.py

from django.db import models
from hos_login.models import Custom_User
import uuid

class ReceiptVoucher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class PaymentVoucher(models.Model):
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class Cashbook(models.Model):
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class AccountLedger(models.Model):
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

class BankAccount(models.Model):
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)
