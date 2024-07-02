# patient/serializers.py
from rest_framework import serializers
from patient.models.models import Patient, PatientBilling, PatientHistory, PatientLedger, PatientReminder, PatientVisitList
from rest_framework.exceptions import PermissionDenied
from django.utils.dateparse import parse_datetime

class PatientSerializer(serializers.ModelSerializer):
    Register_Date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])


    class Meta:
        model = Patient
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

class PatientBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBilling
        fields = '__all__'

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'

class PatientLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientLedger
        fields = '__all__'

class PatientReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientReminder
        fields = '__all__'

class PatientVisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVisitList
        fields = '__all__'
