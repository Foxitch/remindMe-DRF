from django.contrib import admin

from to_do.models import Board, ToDoList


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)
    ordering = ('id', 'name',)


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    pass
