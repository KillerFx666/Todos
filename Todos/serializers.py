from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from Todos.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
