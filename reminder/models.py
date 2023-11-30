from django.db import models
from django.utils import timezone

from reminder.tasks import send_reminder_email


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField(max_length=400)
    delay = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    is_triggered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Reminder, self).save(*args, **kwargs)
        if not self.is_triggered:
            send_reminder_email.apply_async(args=[self.id], eta=timezone.now() + timezone.timedelta(seconds=self.delay))

    def __str__(self) -> str:
        return f'Remind to {self.email} if overdue more than {self.delay} minutes'
