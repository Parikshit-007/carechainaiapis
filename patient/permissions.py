# patient/permissions.py

from rest_framework import permissions

class IsAuthenticatedHospitalOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated and a hospital owner
        if request.user.is_authenticated and request.user.is_hospital:
            # Check if the hospital associated with the patient object matches the logged-in hospital
            return obj.hospital == request.user.hospital
        return False
