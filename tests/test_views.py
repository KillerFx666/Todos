from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from Todos.models import Todo

User = get_user_model()


class TodoViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post('/users/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.token = response.data['access']

    def test_list_todos(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_todo(self):
        todo = Todo.objects.create(title='Test Todo', description='This is a test todo.', user=self.user)
        response = self.client.get(f'/todos/{todo.id}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Test Todo', description='This is a test todo.', user=self.user)
        response = self.client.delete(f'/todos/{todo.id}/')
        self.assertEqual(response.status_code, 204)
