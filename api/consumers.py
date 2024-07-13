import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class StageConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stage_name = None
        self.stage_group_name = None
        # self.stage = None

    def connect(self):
        self.stage_name = self.scope['url_route']['kwargs']['stage_name']
        self.stage_group_name = f"stage_{self.stage_name}"
        # self.stage =

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.stage_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.stage_group_name, self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.stage_group_name, {'type': 'send_stage_message', 'message': message}
        )

    def send_stage_message(self, event):
        self.send(text_data=json.dumps(event))
