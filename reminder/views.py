from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from reminder.models import Reminder
from reminder.serializers import ReminderListSerializer


class ReminderCreateAPIView(RetrieveUpdateDestroyAPIView):
    """
    API for creating Reminders
    permission: IsAdmin
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializer
    permission_classes = (permissions.IsAdminUser,)
