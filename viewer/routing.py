#-*-coding=utf-8-*-

from django.urls import path
from viewer.lib.socketman import socketman

websocket_urlpatterns = [
    path('ws/', socketman),
]
