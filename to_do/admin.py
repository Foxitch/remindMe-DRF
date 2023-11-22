from django.contrib import admin

from to_do.models import Board, ToDoList


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    pass
