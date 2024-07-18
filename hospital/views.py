from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import Hospital
from .serializers import HospitalSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    # queryset = Hospital.objects.filter()
    queryset = Hospital.objects.all()  # Add this line

    serializer_class = HospitalSerializer
    def get_queryset(self):
        # Filter hospitals by the owner (the logged-in user)
        user = self.request.user
        return Hospital.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
