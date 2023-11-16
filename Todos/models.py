from django.db import models
from accounts.models import User


class TodoStatus(models.Choices):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=9, choices=TodoStatus.choices, default=TodoStatus.PENDING, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
