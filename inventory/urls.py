from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from inventory.views.views import (
    MedicineViewSet,
    EquipmentViewSet,
    PatientEquipmentUsageViewSet,
    StockLevelAlertViewSet,
    PurchaseOrderViewSet,
    PatientMedicineEquipmentUsageViewSet,
    InventoryItemViewSet,
)

urlpatterns = [
    path('api/medicines/', MedicineViewSet.as_view({'get': 'list', 'post': 'create'}), name='medicine-list-create'),
    path('api/medicines/<int:pk>/', MedicineViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='medicine-retrieve-update-destroy'),

    path('api/equipment/', EquipmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='equipment-list-create'),
    path('api/equipment/<int:pk>/', EquipmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='equipment-retrieve-update-destroy'),

    path('api/stock-alerts/', StockLevelAlertViewSet.as_view({'get': 'list', 'post': 'create'}), name='stock-level-alert-list-create'),
    path('api/stock-alerts/<int:pk>/', StockLevelAlertViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='stock-level-alert-retrieve-update-destroy'),

    path('api/purchase-orders/', PurchaseOrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='purchase-order-list-create'),
    path('api/purchase-orders/<int:pk>/', PurchaseOrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='purchase-order-retrieve-update-destroy'),

    path('api/inventory-items/', InventoryItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='inventory-item-list-create'),
    path('api/inventory-items/<int:pk>/', InventoryItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='inventory-item-retrieve-update-destroy'),
    path('api/patient-medicine-usage/', PatientMedicineEquipmentUsageViewSet.as_view({'get': 'list', 'post': 'create'}), name='patient-equipment-usage-list-create'),
    path('api/patient-medicine-usage/<int:pk>/', PatientMedicineEquipmentUsageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='patient-equipment-usage-retrieve-update-destroy'),
    path('api/patient-equipment-usage/', PatientEquipmentUsageViewSet.as_view({'get': 'list', 'post': 'create'}), name='patient-equipment-usage-list-create'),
    path('api/patient-equipment-usage/<int:pk>/', PatientEquipmentUsageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='patient-equipment-usage-retrieve-update-destroy'),
]