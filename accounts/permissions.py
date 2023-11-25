from rest_framework.permissions import BasePermission




class IsOwner(BasePermission):
    """
    The IsOwner class is a custom permission class in the Django REST Framework ,
    that allows only the owner of an object to perform write and see operations on it .
    """
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return False
