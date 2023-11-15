from rest_framework import permissions


class IsOwnerOrAdminPermission(permissions.BasePermission):
    """ Check object is owner of staff """

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.user == request.user or request.user.is_staff
