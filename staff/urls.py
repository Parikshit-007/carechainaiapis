from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from staff.views.views import StaffAttendanceListCreateView, StaffShiftListCreateView, StaffLeaveListCreateView, StaffPerformanceListCreateView

urlpatterns = [
    path('attendance/', StaffAttendanceListCreateView.as_view(), name='staff-attendance'),
    path('shift/', StaffShiftListCreateView.as_view(), name='staff-shift'),
    path('leave/', StaffLeaveListCreateView.as_view(), name='staff-leave'),
    path('performance/', StaffPerformanceListCreateView.as_view(), name='staff-performance'),
]
