from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    The IsOwnerOrReadOnly class is a custom permission class in the Django REST Framework ,
    that allows only the owner of an object to perform write operations on it ,
    while allowing read operations for all users
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
