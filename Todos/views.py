from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

