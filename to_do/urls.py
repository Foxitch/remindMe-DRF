from django.urls import include, path
from rest_framework import routers

from to_do.views import (BoardViewSet, TodoCreateApiView, TodoDeleteApiView,
                         TodoListApiView, TodoListUndoneApiView,
                         TodoUpdateApiView)

router = routers.SimpleRouter()
router.register(prefix=r'board', viewset=BoardViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('todo-create/', TodoCreateApiView.as_view()),
    path('todo-list/<int:board>/', TodoListApiView.as_view()),
    path('todo-list-undone/<int:board>/', TodoListUndoneApiView.as_view()),
    path('todo-delete/<int:pk>/', TodoDeleteApiView.as_view()),
    path('todo-update/<int:pk>/', TodoUpdateApiView.as_view()),
]
