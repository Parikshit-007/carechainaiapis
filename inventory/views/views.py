from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework import viewsets
from inventory.models.models import Medicine, Equipment, StockLevelAlert, PurchaseOrder, InventoryItem, PatientEquipmentUsage
from inventory.serializers import (
    MedicineSerializer,
    EquipmentSerializer,
    StockLevelAlertSerializer,
    PurchaseOrderSerializer,
    InventoryItemSerializer,
    PatientEquipmentUsageSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class StockLevelAlertViewSet(viewsets.ModelViewSet):
    queryset = StockLevelAlert.objects.all()
    serializer_class = StockLevelAlertSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer


class PatientEquipmentUsageViewSet(viewsets.ModelViewSet):
    queryset = PatientEquipmentUsage.objects.all()
    serializer_class = PatientEquipmentUsageSerializer
    def create(self, request, *args, **kwargs):
        # Get the 'patient' field from request data
        patient_id = request.data.get('patient')
        print(patient_id)
        
        # Ensure that 'patient_id' is provided in the request data
        if not patient_id:
            return Response({'error': 'Patient ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Print the request data 
        print(request.data)
        
        # Create the serializer instance
        serializer = self.get_serializer(data=request.data)
        
        # Validate the serializer data
        serializer.is_valid(raise_exception=True)
        
        # Save the validated serializer data
        self.perform_create(serializer)
        
        # Get the response data and headers
        headers = self.get_success_headers(serializer.data)
        
        # Return a success response with the created data
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)
