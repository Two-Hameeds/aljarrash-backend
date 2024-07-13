from django.urls import re_path
from .consumers import StageConsumer

websocket_urlpatterns = [
    re_path(r'ws/stage/(?P<stage_name>\w+)/$', StageConsumer.as_asgi()),
]