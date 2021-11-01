import json

from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async
from .models import Message
from django.template import Context, Template

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_group_name = 'chat_%s' % self.room_name
        self.room_group_name = 'chat'

        # Join room group
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )

    async def receive(self, text_data):
        data = json.loads(text_data)
        body = data['body']
        author = data['author']

        new_message = await self.save_message(author=author, body=body)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
            'type': 'chat_message',
            'body': new_message.body,
            'author': new_message.author.username,
            "created": Template("{{ date }}").render(Context({"date": new_message.created})),
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        body = event['body']
        author = event['author']
        created = event['created']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'body': body,
            'author': author,
            'created': created
        }))

    @sync_to_async
    def save_message(self, author, body):
        message = Message.objects.create_message(author=author, body=body)
        return message
