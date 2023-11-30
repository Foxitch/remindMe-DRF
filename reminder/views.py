from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from reminder.models import Reminder
from reminder.serializers import ReminderListSerializer


class ReminderViewSet(ModelViewSet):
    """
    API for creating Reminders
    permission: IsAdmin
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializer
    permission_classes = (permissions.IsAdminUser,)
