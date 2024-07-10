






# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import Custom_User
from .backends import CustomUserModelBackend
from .models import Custom_User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Custom_User
        fields= ('id','email', 'username')    
class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Custom_User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Custom_User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
           # hospital=validated_data['hospital'],
        )

        user.set_password(validated_data['password'])
        user.save()
     

        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    passsword = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Custom_User
        fields = ['hospital', 'email', 'username', 'password']

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance

#         return user
@csrf_exempt
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        print(username)
        print(password)
        if username and password:
            # Instantiate the custom authentication backend
            backend = CustomUserModelBackend()
            user = backend.authenticate(request=self.context.get('request'), username=username, password=password)
#            print('dekh',user)
            if user:
                return user
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('hospital','email', 'username', 'password', 'password2')

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             hospital=validated_data['hospital'],
#         )

#         user.set_password(validated_data['password'])
#         user.save()

#         return user


