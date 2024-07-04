import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import api.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aljarrash_backend.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.routing.websocket_urlpatterns
        )
    ),
})
