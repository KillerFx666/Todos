from Todos.models import Todo
from Todos.serializers import TodoSerializer
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import serializers

User = get_user_model()


class TestTodoSerializer(APITestCase):

    def test_serialize_valid_todo_object(self):
        user = User.objects.create(username='amirhossein')
        todo = Todo.objects.create(title='Test Todo', description='Test Description', status='PENDING', user=user)

        serializer = TodoSerializer(todo)
        self.assertEqual(serializer.data['title'], 'Test Todo')
        self.assertEqual(serializer.data['description'], 'Test Description')

    def test_validation_error_title_too_long(self):
        user = User.objects.create(username='amirhossein')
        todo = Todo(title='A' * 256, description='Test Description', status='PENDING', user=user)

        serializer = TodoSerializer(data={
            'title': todo.title,
            'description': todo.description,
            'status': todo.status,
            'user': str(todo.user.id)
        })

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_validation_error_description_too_long(self):
        user = User.objects.create(username='amirhossein')
        todo = Todo(title='Test Todo', description='A' * 501, status='PENDING', user=user)

        serializer = TodoSerializer(data={
            'title': todo.title,
            'description': todo.description,
            'status': todo.status,
            'user': str(todo.user.id)
        })

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_validation_error_invalid_status(self):
        user = User.objects.create(username='amirhossein')
        todo = Todo(title='Test Todo', description='Test Description', status='INVALID', user=user)

        serializer = TodoSerializer(data={
            'title': todo.title,
            'description': todo.description,
            'status': todo.status,
            'user': str(todo.user.id)
        })

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
