






# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import User
from .backends import CustomUserModelBackend
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

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
            print('dekh',user)
            if user:
                return user
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('hospital','email', 'username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            hospital=validated_data['hospital'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user













# # serializers.py

# from rest_framework import serializers
# from .models import User, Hospital
# from rest_framework_simplejwt.tokens import RefreshToken
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['id', 'hospital', 'username', 'password', 'email']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create(
#             hospital=validated_data['hospital'],
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         print(validated_data)
#         refresh = RefreshToken.for_user(user)
        
#         # Return serialized data of the created user along with tokens
#         return {
#             'user': self.to_representation(user),  # Ensure user object is returned with key 'user'
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
# # # serializers.py
# # from rest_framework import serializers
# # from .models import Hospital, User
# # from rest_framework_simplejwt.tokens import RefreshToken

# # class HospitalSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Hospital
# #         fields = '__all__'
        
# # class UserSerializer(serializers.ModelSerializer):
# #     password = serializers.CharField(write_only=True)

# #     class Meta:
# #         model = User
# #         fields = ['id', 'hospital', 'username', 'password', 'email']
# #         extra_kwargs = {'password': {'write_only': True}}

# #     def create(self, validated_data):
# #         user = User.objects.create(
# #             hospital=validated_data['hospital'],
# #             username=validated_data['username'],
# #             email=validated_data['email'],
# #         )
# #         user.set_password(validated_data['password'])
# #         user.save()
# #         print(validated_data)
# #         refresh = RefreshToken.for_user(user)
        
# #         # Return serialized data of the created user along with tokens
# #         return {
# #             'user': self.to_representation(user),  # Ensure user object is returned with key 'user'
# #             'refresh': str(refresh),
# #             'access': str(refresh.access_token)
# #         }
# # # class UserSerializer(serializers.ModelSerializer):
# # #     password = serializers.CharField(write_only=True)  # Define the password field here

# # #     class Meta:
# # #         model = User
# # #         fields = ['id', 'hospital', 'username', 'password','email']
# # #         extra_kwargs = {'password': {'write_only': True}}

# # #     def create(self, validated_data):
# # #         user = User.objects.create(
# # #             hospital=validated_data['hospital'],
# # #             username=validated_data['username']
# # #         )
# # #         print('bhai data',validated_data)
# # #         user.set_password(validated_data['password'])
# # #         user.save()
# # #         return user
