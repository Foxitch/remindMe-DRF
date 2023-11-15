from django.urls import path

from to_do.views import (BoardCreateApiView, BoardListApiView,
                         BoardUpdateDestroyApiView, TodoCreateApiView,
                         TodoListApiView, TodoListUndoneApiView, TodoDeleteApiView, TodoUpdateApiView)

urlpatterns = [
    path('board-list/', BoardListApiView.as_view()),
    path('board-create/', BoardCreateApiView.as_view()),
    path('board-rud/<int:pk>/', BoardUpdateDestroyApiView.as_view()),
    path('todo-create/', TodoCreateApiView.as_view()),
    path('todo-list/<int:board>/', TodoListApiView.as_view()),
    path('todo-list-undone/<int:board>/', TodoListUndoneApiView.as_view()),
    path('todo-delete/<int:pk>/', TodoDeleteApiView.as_view()),
    path('todo-update/<int:pk>/', TodoUpdateApiView.as_view()),
]
