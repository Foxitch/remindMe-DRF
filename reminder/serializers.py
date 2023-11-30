from rest_framework import serializers

from reminder.models import Reminder


class ReminderListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    text = serializers.CharField(max_length=400)
    delay = serializers.IntegerField(default=10)

    class Meta:
        model = Reminder
        fields = '__all__'
