from django.db import models
from hos_login.models import Custom_User  # Assuming Custom_User is your user model
from patient.models.models import Patient  # Assuming Patient is your patient model

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

class StockLevelAlert(models.Model):
    inventory_item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    threshold_quantity = models.PositiveIntegerField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"{self.inventory_item} - Threshold: {self.threshold_quantity}"

class PurchaseOrder(models.Model):
    inventory_item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    quantity_to_order = models.PositiveIntegerField()
    order_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"{self.inventory_item} - Quantity: {self.quantity_to_order}"

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

class PatientEquipmentUsage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField(default=0)
    usage_date = models.DateField(auto_now_add=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Custom_User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"Patient ID: {self.patient}, Equipment: {self.equipment.name}, Quantity Used: {self.quantity_used}, Usage Date: {self.usage_date}"
