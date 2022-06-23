import ipdb
from rest_framework import permissions


class IsLucira(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        # ipdb.set_trace()
        # if request.method in ['GET', "HEAD", "OPTIONS"]

        if request.method in permissions.SAFE_METHODS:
            return True

        return "lucira" in request.user.email


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
