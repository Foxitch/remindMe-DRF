from django.db.models import QuerySet
from overrides import override
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from to_do.models import Board, ToDoList
from to_do.permissions import IsOwnerOrAdminPermission
from to_do.serializers import BoardSerializer, ToDoListApiViewSerializer


class BoardViewSet(ModelViewSet):
    """
    API for CRUD boards with counts from todo_list for each board
    permission: -IsAuthOrReadOnly
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @override
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = self.get_serializer(queryset, many=True).data
        for board_data in data:
            board_id = board_data['id']
            todo_count = ToDoList.objects.filter(board_id=board_id).count()
            board_data['todo_count'] = todo_count
        return Response(data)


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
