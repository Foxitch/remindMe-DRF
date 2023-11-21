from rest_framework import generics, permissions
from reminder.models import Reminder
from reminder.serializers import ReminderListSerializer


class ReminderCreateAPIView(generics.CreateAPIView):
    """
    API for creating Reminders
    permission: IsAdmin
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializer
    permission_classes = (permissions.IsAdminUser,)


class ReminderListAPIView(generics.ListAPIView):
    """
    API for getting List of Reminders
    permission: IsAdmin
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializer
    permission_classes = (permissions.IsAdminUser,)


class ReminderDeleteAPIView(generics.DestroyAPIView):
    """
    API for deleting Reminders
    permission: IsAdmin
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializer
    permission_classes = (permissions.IsAdminUser,)
