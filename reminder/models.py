from django.db import models
from django.utils.timezone import now


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField(max_length=400)
    delay = models.IntegerField(default=10)
    due_date = models.DateTimeField(default=now, blank=True)

    def __str__(self) -> str:
        return f'Remind to {self.email} if overdue more than {self.delay} minutes'
