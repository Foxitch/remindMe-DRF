from django.db.models import Count
from rest_framework import generics, permissions

from to_do.models import Board
from to_do.serializers import BoardListApiViewSerializer, BoardCreateApiViewSerializer


class BoardListApiView(generics.ListAPIView):
    """
    API for Boards with counts from todo_list for each board
    permission: -IsAuth
    """

    serializer_class = BoardListApiViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        queryset = Board.objects.annotate(count=Count('todolist__board'))
        return queryset


class BoardCreateApiView(generics.CreateAPIView):
    """
    API for creating Board
    permission: -IsAdmin
    """

    serializer_class = BoardCreateApiViewSerializer
    permission_classes = [permissions.IsAdminUser,]


class BoardUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    API for updating and deleting Boards
    permission: -IsAdmin
    """

    serializer_class = BoardCreateApiViewSerializer
    permission_classes = [permissions.IsAdminUser,]
    queryset = Board.objects.all()
