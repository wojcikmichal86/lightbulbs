from channels.generic.websocket import AsyncWebsocketConsumer
from myapi.models import Lightbulb, Blinds, Temperature
from myapi.serializers import LightbulbSerializer, BlindsSerializer, TemperatureSerializer
import json
from channels.db import database_sync_to_async
from asyncio import sleep


class LightbulbConsumer(AsyncWebsocketConsumer): #fetches the data from the DB and sends it to the websocket
    async def connect(self): #connects to the DB
        await self.accept()
        while True:
            await self.fetch_data()
            await sleep(0.5) #sleeps is necessary so the browser doesn't crash


    async def fetch_data(self):
        message = await self.get_objects()
        await self.send(json.dumps(message))


    @database_sync_to_async #turns the asyncronous websocket to syncronous DB
    def get_objects(self):
        devices = Lightbulb.objects.get(id=1) #gets the first object from the model
        serializer = LightbulbSerializer(devices, many=False) #uses the serializer to turn it into dict
        return serializer.data


class BlindsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await self.fetch_data()
            await sleep(0.5)


    async def fetch_data(self):
        message = await self.get_objects()
        await self.send(json.dumps(message))


    @database_sync_to_async
    def get_objects(self):
        devices = Blinds.objects.get(id=1)
        serializer = BlindsSerializer(devices, many=False)
        return serializer.data


class TemperatureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await self.fetch_data()
            await sleep(0.5)


    async def fetch_data(self):
        message = await self.get_objects()
        await self.send(json.dumps(message))




    @database_sync_to_async
    def get_objects(self):
        devices = Temperature.objects.get(id=1)
        serializer = TemperatureSerializer(devices, many=False)
        return serializer.data