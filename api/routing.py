from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/stage/(?P<stage_name>\w+)/$', consumers.StageConsumer.as_asgi()),
]