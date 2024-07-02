from django.urls import path
from staff.views.views import StaffListCreateView, StaffAttendanceListCreateView, StaffShiftListCreateView, StaffLeaveListCreateView, StaffPerformanceListCreateView

urlpatterns = [
    path('staff/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('attendance/', StaffAttendanceListCreateView.as_view(), name='staff-attendance'),
    path('shift/', StaffShiftListCreateView.as_view(), name='staff-shift'),
    path('leave/', StaffLeaveListCreateView.as_view(), name='staff-leave'),
    path('performance/', StaffPerformanceListCreateView.as_view(), name='staff-performance'),
]
