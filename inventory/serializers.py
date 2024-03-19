from rest_framework import serializers
from inventory.models.models import Medicine, Equipment, PatientEquipmentUsage, StockLevelAlert, PurchaseOrder, InventoryItem

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class StockLevelAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockLevelAlert
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class PatientEquipmentUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientEquipmentUsage
        fields = '__all__'