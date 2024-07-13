import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.stage_name = self.scope['url_route']['kwargs']['stage_name']
        self.stage_group_name = f'stage_{self.stage_name}'

        await self.channel_layer.group_add(
            self.stage_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.stage_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': messgae
        }))


    async def send_stage_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': messgae
        }))