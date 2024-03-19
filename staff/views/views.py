from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from staff.models.models import StaffAttendance, StaffShift, StaffLeave, StaffPerformance
from staff.serializers import StaffAttendanceSerializer, StaffShiftSerializer, StaffLeaveSerializer, StaffPerformanceSerializer

class StaffAttendanceListCreateView(generics.ListCreateAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [IsAuthenticated]

class StaffShiftListCreateView(generics.ListCreateAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [IsAuthenticated]

class StaffLeaveListCreateView(generics.ListCreateAPIView):
    queryset = StaffLeave.objects.all()
    serializer_class = StaffLeaveSerializer
    permission_classes = [IsAuthenticated]

class StaffPerformanceListCreateView(generics.ListCreateAPIView):
    queryset = StaffPerformance.objects.all()
    serializer_class = StaffPerformanceSerializer
    permission_classes = [IsAuthenticated]
