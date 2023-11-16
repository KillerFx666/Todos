from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory

from Todos.permissions import IsOwnerOrReadOnly

User = get_user_model()


class TestIsOwnerOrReadOnly(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='erfan', email='amirgolami131385@gmail.com', password='test_password')

    def test_get_method_authenticated_user(self):
        request = self.factory.get('/test_url')
        request.user = self.user
        permission = IsOwnerOrReadOnly()
        obj = self.user

        self.assertTrue(permission.has_object_permission(request, None, obj))

    def test_get_method_unauthenticated_user(self):
        request = self.factory.get('/test_url')
        request.user = AnonymousUser()
        permission = IsOwnerOrReadOnly()
        obj = User.objects.create_user(
            username='amirhossein', email='amirhossein131385@gmail.com', password='test_password')

        self.assertTrue(permission.has_object_permission(request, None, obj))

    def test_object_without_user_attribute(self):
        request = self.factory.get('/test_url')
        request.user = self.user
        permission = IsOwnerOrReadOnly()
        obj = 'This is not a user object'

        self.assertTrue(permission.has_object_permission(request, None, obj))
