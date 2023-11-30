from django.urls import path, include
from rest_framework import routers

from reminder.views import ReminderViewSet

router = routers.SimpleRouter()
router.register(prefix=r'reminder', viewset=ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
