from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_reminder_email(reminder_id: int) -> None:
    from reminder.models import Reminder

    reminder = Reminder.objects.get(id=reminder_id)
    send_mail(
        'Reminder',
        reminder.text,
        'noreply@example.com',
        [reminder.email],
        fail_silently=False,
    )
    reminder.is_triggered = True
    reminder.save()
