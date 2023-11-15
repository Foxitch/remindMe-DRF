from django.db.models import Count, QuerySet
from rest_framework import generics, permissions

from to_do.models import Board, ToDoList
from to_do.permissions import IsOwnerOrAdminPermission
from to_do.serializers import (BoardCreateApiViewSerializer,
                               BoardListApiViewSerializer,
                               ToDoListApiViewSerializer)


class BoardListApiView(generics.ListAPIView):
    """
    API for Boards with counts from todo_list for each board
    permission: -IsAuth
    """

    serializer_class = BoardListApiViewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        queryset = Board.objects.annotate(count=Count('todolist__board'))
        return queryset


class BoardCreateApiView(generics.CreateAPIView):
    """
    API for creating Board
    permission: -IsAdmin
    """

    serializer_class = BoardCreateApiViewSerializer
    permission_classes = (permissions.IsAdminUser,)


class BoardUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    API for updating and deleting Boards
    permission: -IsAdmin
    """

    serializer_class = BoardCreateApiViewSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = Board.objects.all()


class TodoCreateApiView(generics.CreateAPIView):
    """
    API for to do creating
    permission: -IsAdmin
    """

    serializer_class = ToDoListApiViewSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = ToDoList.objects.all()


class TodoListApiView(generics.ListAPIView):
    """
    API for getting list of all ToDos
    permission: -IsAuth
    """
    serializer_class = ToDoListApiViewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        queryset = ToDoList.objects.filter(board=self.kwargs['board'])
        return queryset


class TodoListUndoneApiView(generics.ListAPIView):
    """
    API for getting list of undones todos
    permission: -IsAuth
    """
    serializer_class = ToDoListApiViewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        queryset = ToDoList.objects.filter(done=self.kwargs['board']).filter(done=False)
        return queryset


class TodoDeleteApiView(generics.DestroyAPIView):
    """
    API for deleting todos
    permission: -IsAdmin
    """
    serializer_class = ToDoListApiViewSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = ToDoList.objects.all()


class TodoUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    API for update todos
    permission: -IsOwnerOrStaff
    """
    serializer_class = ToDoListApiViewSerializer
    permission_classes = (IsOwnerOrAdminPermission,)
    queryset = ToDoList.objects.all()
