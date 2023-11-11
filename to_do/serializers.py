from rest_framework import serializers
from models import Board, ToDoList


class BoardCreateApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', ]


class ToDoListApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'


class BoardListApiViewSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    count = serializers.IntegerField()
