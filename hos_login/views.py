import statistics
from urllib import response
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Hospital, User
from .serializers import HospitalSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
class HospitalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
