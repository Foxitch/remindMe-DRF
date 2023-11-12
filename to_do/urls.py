from django.urls import path, include
from to_do.views import BoardListApiView, BoardCreateApiView, BoardUpdateDestroyApiView


urlpatterns = [
    path('board-list/', BoardListApiView.as_view()),
    path('board-create/', BoardCreateApiView.as_view()),
    path('board-rud/<int:pk>/', BoardUpdateDestroyApiView.as_view()),
]
