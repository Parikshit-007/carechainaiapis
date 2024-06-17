# ipd/serializers.py
from rest_framework import serializers
from ipd.models.models import Bed,Ward, DischargeHistory,BedAllocation , BedAvailability, BedBooking , BedStatusUpdate ,WardWiseBedReport, IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport, IPDDepositReport, IPDDischargeReport, DepartmentReport, WardWiseReport, DoctorWiseReport, TPAReport
from rest_framework.exceptions import PermissionDenied

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'
        read_only_fields = ['owner']  # owner ko read-only banate hain

    def create(self, validated_data):
        # current user ko fetch karna
        user = self.context['request'].user

        # check if the user is authenticated
        if not user.is_authenticated:
            raise PermissionDenied("Authentication required to create a patient.")

        # set the owner field
        validated_data['owner'] = user

        return super().create(validated_data)

class BedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 
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
    admission = serializers.PrimaryKeyRelatedField(queryset=IPDRegistration.objects.all())
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = IPDDischarge
        fields = ('discharge_id', 'admission', 'discharge_date', 'discharge_summary', 'owner')
    def create(self, validated_data):
        discharge = super().create(validated_data)
        # Additional logic can go here if needed
        return discharge

    def update(self, instance, validated_data):
        discharge = super().update(instance, validated_data)
        # Additional logic can go here if needed
        return discharge
# class IPDDischargeSerializer(serializers.ModelSerializer):
#     owner = serializers.PrimaryKeyRelatedField(read_only=True)

#     class Meta:
#         model = IPDDischarge
#         fields = ['admission', 'discharge_date', 'owner']

#     def create(self, validated_data):
#         request = self.context.get('request')
#         if request and hasattr(request, 'user'):
#             validated_data['owner'] = request.user
#         return super().create(validated_data)


class IPDAdmitReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDAdmitReport
        fields = '__all__'
class DischargeHistorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = DischargeHistory
        fields= '__all__'
class IPDDepositReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = IPDDepositReport
        fields = '__all__'

class IPDDischargeReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 

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