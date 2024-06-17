# views.py

from rest_framework import generics, filters
from doctor.models.models import Doctor
from doctor.serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'specialty']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
