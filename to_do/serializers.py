from rest_framework import serializers
from to_do.models import Board, ToDoList


class BoardCreateApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', ]


class ToDoListApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'


class BoardListApiViewSerializer(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()
