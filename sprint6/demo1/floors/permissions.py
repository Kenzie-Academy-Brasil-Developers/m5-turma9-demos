import ipdb
from parking_lots.models import ParkingLot
from rest_framework import permissions


# self.check_permission(request, obj)
class IsOwnerOrReadOnly(permissions.BasePermission):
    # ipdb.set_trace()
    def has_object_permission(self, request, view, parking_lot: ParkingLot):
        if request.method in permissions.SAFE_METHODS:
            return True

        return parking_lot.owner == request.user
