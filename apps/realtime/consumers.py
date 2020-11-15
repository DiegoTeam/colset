import json
from channels.generic.websocket import JsonWebsocketConsumer


class TestConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content, **kwargs):
        self.send(text_data=json.dumps({
            'content': content
        }))
