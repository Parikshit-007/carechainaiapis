# ipd/serializers.py
from rest_framework import serializers
from ipd.models.models import Bed,Ward, BedAllocation , BedAvailability, BedBooking , BedStatusUpdate ,WardWiseBedReport, IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport, IPDDepositReport, IPDDischargeReport, DepartmentReport, WardWiseReport, DoctorWiseReport, TPAReport


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'
class BedSerializer(serializers.ModelSerializer):
    ward = WardSerializer()
    class Meta:
        model = Bed
        fields = '__all__'  
    def get_is_available(self, obj):
        return obj.is_available()          

class BedBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedBooking
        fields = '__all__'

class BedAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedAllocation
        fields = '__all__'

class BedStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedStatusUpdate
        fields = '__all__'

class BedAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BedAvailability
        fields = '__all__'

class IPDRegistrationSerializer(serializers.ModelSerializer):
    # bed = serializers.PrimaryKeyRelatedField(queryset=Bed.objects.none())
    # def __init__(self, *args, **kwargs):
    #     available_beds = kwargs.pop('available_beds', None)
    #     super().__init__(*args, **kwargs)
    #     if available_beds is not None:
    #         self.fields['bed'].queryset = available_beds
  

    class Meta:
        model = IPDRegistration
        fields = '__all__'
        
class IPDDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDeposit
        fields = '__all__'

class IPDDischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDischarge
        fields = '__all__'

class IPDAdmitReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDAdmitReport
        fields = '__all__'

class IPDDepositReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDepositReport
        fields = '__all__'

class IPDDischargeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDischargeReport
        fields = '__all__'

class DepartmentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentReport
        fields = '__all__'

class WardWiseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardWiseReport
        fields = '__all__'

class DoctorWiseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorWiseReport
        fields = '__all__'

class TPAReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPAReport
        fields = '__all__'