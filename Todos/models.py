from django.db import models

# Create your models here.


class TodoStatus(models.Choices):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=9, choices=TodoStatus.choices, default=TodoStatus.PENDING)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
