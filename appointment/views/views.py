from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appointment.models.models import Appointment
from appointment.serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return appointments that belong to the authenticated user
        return Appointment.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if the appointment slot is available
           # date = serializer.validated_data['date']
            time_slot = serializer.validated_data['time_slot']
            if Appointment.objects.filter( time_slot=time_slot).exists():
                return Response({'error': 'Appointment slot already booked.'}, status=status.HTTP_400_BAD_REQUEST)
            # Create the appointment
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return appointments that belong to the authenticated user
        return Appointment.objects.filter(owner=self.request.user)