from django.urls import path

from reminder.views import ReminderListAPIView, ReminderCreateAPIView, ReminderDeleteAPIView


urlpatterns = [
    path('reminders-list/', ReminderListAPIView.as_view()),
    path('reminders-create/', ReminderCreateAPIView.as_view()),
    path('reminders-delete/<int:pk>/', ReminderDeleteAPIView.as_view()),
]
