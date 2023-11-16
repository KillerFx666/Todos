from accounts.models import User
from rest_framework import serializers
from Todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'user', 'status', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']
