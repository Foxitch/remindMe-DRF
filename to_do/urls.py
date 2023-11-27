from django.urls import include, path
from rest_framework import routers

from to_do.views import BoardViewSet, TodoViewSet

router = routers.SimpleRouter()
router.register(prefix=r'board', viewset=BoardViewSet)
router.register(prefix=r'to_do', viewset=TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
