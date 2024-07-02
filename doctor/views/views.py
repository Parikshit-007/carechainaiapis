from rest_framework import generics, filters
from doctor.models.models import Doctor
from doctor.serializers import DoctorSerializer
from rest_framework.exceptions import PermissionDenied

class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'specialty']
   
    def get_queryset(self):
        return Doctor.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.filter(owner=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied("You do not have permission to access this resource.")
        return obj

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)