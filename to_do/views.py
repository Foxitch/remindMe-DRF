from overrides import override
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from remindMe.core.pagination import CustomPagination
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
    def list(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        data = self.get_serializer(queryset, many=True).data
        for board_data in data:
            board_id = board_data['id']
            todo_count = ToDoList.objects.filter(board_id=board_id).count()
            board_data['todo_count'] = todo_count
        return Response(data=data)


class TodoViewSet(ModelViewSet):
    """
    API for CRUD to_do, GET has filter by status
    permission: -IsOwnerOrAdminPermission
    """

    serializer_class = ToDoListApiViewSerializer
    permission_classes = (IsOwnerOrAdminPermission,)
    queryset = ToDoList.objects.all()
    filterset_fields = ('done',)
