from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Class for custom permission
    Ensures only profile owner can update or delete object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
