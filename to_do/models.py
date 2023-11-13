from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f'Board {self.name}'


class ToDoList(models.Model):
    title = models.CharField(max_length=32)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    board = models.ForeignKey(to=Board, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'ToDoList {self.title} created at {self.created}'
