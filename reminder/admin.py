from django.contrib import admin

from reminder.models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    pass
