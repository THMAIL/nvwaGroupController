# -*-coding=utf-8-*-

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import viewer.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        viewer.routing.websocket_urlpatterns

    ),
})
