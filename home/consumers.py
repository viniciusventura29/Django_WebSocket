from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint
from time import sleep
import json


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({'message': randint(1,100)}))
