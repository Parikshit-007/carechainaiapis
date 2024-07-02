from rest_framework import serializers
from staff.models.models import Staff, StaffAttendance, StaffShift, StaffLeave, StaffPerformance

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = '__all__'

class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'

class StaffLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLeave
        fields = '__all__'

class StaffPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPerformance
        fields = '__all__'
