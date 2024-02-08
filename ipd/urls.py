from django.urls import path
from ipd.views.views import (
    IPDRegistrationListCreateView, IPDRegistrationRetrieveUpdateDestroyView,
    IPDDepositListCreateView, IPDDepositRetrieveUpdateDestroyView,
    IPDDischargeListCreateView, IPDDischargeRetrieveUpdateDestroyView,
    IPDAdmitReportListCreateView, IPDAdmitReportRetrieveUpdateDestroyView,
    IPDDepositReportListCreateView, IPDDepositReportRetrieveUpdateDestroyView,
    IPDDischargeReportListCreateView, IPDDischargeReportRetrieveUpdateDestroyView,
    DepartmentReportListCreateView, DepartmentReportRetrieveUpdateDestroyView, WardListCreateView, WardRetrieveUpdateDestroyView,
    WardWiseReportListCreateView, WardWiseReportRetrieveUpdateDestroyView,
    DoctorWiseReportListCreateView, DoctorWiseReportRetrieveUpdateDestroyView,
    TPAReportListCreateView, TPAReportRetrieveUpdateDestroyView,
    # Import the newly added views
    BedListCreateView, BedRetrieveUpdateDestroyView,
    BedBookingListCreateView, BedBookingRetrieveUpdateDestroyView,
    BedAllocationListCreateView, BedAllocationRetrieveUpdateDestroyView,
    BedStatusUpdateListCreateView, BedStatusUpdateRetrieveUpdateDestroyView,
    BedAvailabilityListCreateView, BedAvailabilityRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('ipd-registrations/', IPDRegistrationListCreateView.as_view(), name='ipd-registration-list-create'),
    path('ipd-registrations/<int:pk>/', IPDRegistrationRetrieveUpdateDestroyView.as_view(), name='ipd-registration-retrieve-update-destroy'),

    path('ipd-deposits/', IPDDepositListCreateView.as_view(), name='ipd-deposit-list-create'),
    path('ipd-deposits/<int:pk>/', IPDDepositRetrieveUpdateDestroyView.as_view(), name='ipd-deposit-retrieve-update-destroy'),

    path('ipd-discharges/', IPDDischargeListCreateView.as_view(), name='ipd-discharge-list-create'),
    path('ipd-discharges/<int:pk>/', IPDDischargeRetrieveUpdateDestroyView.as_view(), name='ipd-discharge-retrieve-update-destroy'),

    path('ipd-admit-reports/', IPDAdmitReportListCreateView.as_view(), name='ipd-admit-report-list-create'),
    path('ipd-admit-reports/<int:pk>/', IPDAdmitReportRetrieveUpdateDestroyView.as_view(), name='ipd-admit-report-retrieve-update-destroy'),

    path('ipd-deposit-reports/', IPDDepositReportListCreateView.as_view(), name='ipd-deposit-report-list-create'),
    path('ipd-deposit-reports/<int:pk>/', IPDDepositReportRetrieveUpdateDestroyView.as_view(), name='ipd-deposit-report-retrieve-update-destroy'),

    path('ipd-discharge-reports/', IPDDischargeReportListCreateView.as_view(), name='ipd-discharge-report-list-create'),
    path('ipd-discharge-reports/<int:pk>/', IPDDischargeReportRetrieveUpdateDestroyView.as_view(), name='ipd-discharge-report-retrieve-update-destroy'),

    path('department-reports/', DepartmentReportListCreateView.as_view(), name='department-report-list-create'),
    path('department-reports/<int:pk>/', DepartmentReportRetrieveUpdateDestroyView.as_view(), name='department-report-retrieve-update-destroy'),
    path('wards/', WardListCreateView.as_view(), name='ward-list-create'),
    path('wards/<int:pk>/', WardRetrieveUpdateDestroyView.as_view(), name='ward-retrieve-update-destroy'),
    path('ward-wise-reports/', WardWiseReportListCreateView.as_view(), name='ward-wise-report-list-create'),
    path('ward-wise-reports/<int:pk>/', WardWiseReportRetrieveUpdateDestroyView.as_view(), name='ward-wise-report-retrieve-update-destroy'),

    path('doctor-wise-reports/', DoctorWiseReportListCreateView.as_view(), name='doctor-wise-report-list-create'),
    path('doctor-wise-reports/<int:pk>/', DoctorWiseReportRetrieveUpdateDestroyView.as_view(), name='doctor-wise-report-retrieve-update-destroy'),

    path('tpa-reports/', TPAReportListCreateView.as_view(), name='tpa-report-list-create'),
    path('tpa-reports/<int:pk>/', TPAReportRetrieveUpdateDestroyView.as_view(), name='tpa-report-retrieve-update-destroy'),

    # Add URLs for Bed-related views
    path('beds/', BedListCreateView.as_view(), name='bed-list-create'),
    path('beds/<int:pk>/', BedRetrieveUpdateDestroyView.as_view(), name='bed-retrieve-update-destroy'),

    path('bed-bookings/', BedBookingListCreateView.as_view(), name='bed-booking-list-create'),
    path('bed-bookings/<int:pk>/', BedBookingRetrieveUpdateDestroyView.as_view(), name='bed-booking-retrieve-update-destroy'),

    path('bed-allocations/', BedAllocationListCreateView.as_view(), name='bed-allocation-list-create'),
    path('bed-allocations/<int:pk>/', BedAllocationRetrieveUpdateDestroyView.as_view(), name='bed-allocation-retrieve-update-destroy'),

    path('bed-status-updates/', BedStatusUpdateListCreateView.as_view(), name='bed-status-update-list-create'),
    path('bed-status-updates/<int:pk>/', BedStatusUpdateRetrieveUpdateDestroyView.as_view(), name='bed-status-update-retrieve-update-destroy'),

    path('bed-availabilities/', BedAvailabilityListCreateView.as_view(), name='bed-availability-list-create'),
    path('bed-availabilities/<int:pk>/', BedAvailabilityRetrieveUpdateDestroyView.as_view(), name='bed-availability-retrieve-update-destroy'),
]
