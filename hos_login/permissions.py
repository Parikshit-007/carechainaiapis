# ipd/permissions.py

from rest_framework import permissions

class IsHospitalOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Implement logic to check if the user has ownership over the hospital related to the patient
        return obj.hospital == request.user.hospital
