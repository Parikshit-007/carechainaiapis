# serializers.py
from rest_framework import serializers
from .models import Hospital, User

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Define the password field here

    class Meta:
        model = User
        fields = ['id', 'hospital', 'username', 'password','email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            hospital=validated_data['hospital'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
