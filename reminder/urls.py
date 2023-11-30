from django.urls import path

from reminder.views import ReminderCreateAPIView

urlpatterns = [
    path('reminders/', ReminderCreateAPIView.as_view()),
]
