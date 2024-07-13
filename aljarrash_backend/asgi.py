import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import api.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aljarrash_backend.settings")

# TODO: use AuthMiddlewareStack
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(api.routing.websocket_urlpatterns),
    }
)
