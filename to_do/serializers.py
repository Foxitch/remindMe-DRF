from rest_framework import serializers

from to_do.models import Board, ToDoList


class ToDoListApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Board
        fields = '__all__'
