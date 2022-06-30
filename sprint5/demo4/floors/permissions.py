import ipdb
from rest_framework import permissions

from .models import Floor


class IsOwnerOrReadOnly(permissions.BasePermission):
    # ipdb.set_trace()
    def has_object_permission(self, request, view, obj: Floor):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.parking_lot.owner == request.user
