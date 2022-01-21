from channels.generic.websocket import AsyncWebsocketConsumer
from data_api.models import Senior
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from django.core.cache import cache
import json


DEVICE_TIMEOUT = 60 * 5
MAX_DATA_ARRAY_LEN = 10


class SensorDataConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.device_id = 'test'
        self.device_group_name = self.device_id
        await self.channel_layer.group_add(
            self.device_group_name,
            self.channel_name
        )

        await self.accept()
        # print("#######CONNECTED############")
        # print(self.device_group_name)



    async def disconnect(self, code):
        # global onlineSeniorsDict

        await self.channel_layer.group_discard(
            self.device_group_name,
            self.channel_name
        )
        # print("DISCONNECED CODE: ",code)
        # print("Device IDL ", self.device_id)

    async def receive(self, text_data=None):
        # global onlineSeniorsDict
        data = json.loads(text_data)
        device_id = data['device_id']

        if data["command"] == "new":
            device_id = data.get("device_id")
            senior = await sync_to_async(Senior.objects.get, thread_sensitive=True)(device_id=device_id)
            data["command"] = "new"
            data["name"] = senior.name
            data["room_no"] = senior.room_no
            data["device_type"] = senior.device_type
            data["gender"] = senior.gender
            data["data"] = [{"value": 0, "time": 0}]  # Create list to store sensor data
        elif data["command"] == "update":
            pass
        elif data["command"] == "close":
            pass
        else:
            print("unknown data message")


        await self.channel_layer.group_send(
            self.device_group_name,{
                "type": 'send_message_to_frontend',
                "message": data
            }
        )

    async def send_message_to_frontend(self, event):
        # Receive message from room group
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))