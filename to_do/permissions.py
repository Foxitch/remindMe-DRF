from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsOwnerOrAdminPermission(permissions.BasePermission):
    """ Check object is owner of staff """

    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        return obj.user == request.user or request.user.is_staff
