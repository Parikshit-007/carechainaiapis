from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from staff.models.models import Staff, StaffAttendance, StaffShift, StaffLeave, StaffPerformance
from staff.serializers import StaffSerializer, StaffAttendanceSerializer, StaffShiftSerializer, StaffLeaveSerializer, StaffPerformanceSerializer

class StaffListCreateView(generics.ListCreateAPIView):
    #queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Staff.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class StaffAttendanceListCreateView(generics.ListCreateAPIView):
   # queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return StaffAttendance.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class StaffShiftListCreateView(generics.ListCreateAPIView):
    #queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return StaffShift.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class StaffLeaveListCreateView(generics.ListCreateAPIView):
    #queryset = StaffLeave.objects.all()
    serializer_class = StaffLeaveSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return StaffLeave.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class StaffPerformanceListCreateView(generics.ListCreateAPIView):
    #queryset = StaffPerformance.objects.all()
    serializer_class = StaffPerformanceSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return StaffPerformance.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
