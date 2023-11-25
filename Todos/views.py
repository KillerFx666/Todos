from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class TodoViewSet(viewsets.ModelViewSet):
    """
    The TodoViewSet class is a viewset that provides CRUD operations for the Todo model.
    It uses the TodoSerializer to serialize and deserialize data,
    and it has permission classes to ensure that only authenticated users can access the endpoints,
    and that only the owner of a todo can modify it
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        return super().get_permissions() + [IsOwnerOrReadOnly()]

    def get_queryset(self):
        self.get_permissions()
        return super().get_queryset()
