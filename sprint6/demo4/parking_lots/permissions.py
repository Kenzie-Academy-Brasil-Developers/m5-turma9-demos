from rest_framework import permissions

from .models import ParkingLot


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: ParkingLot):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
