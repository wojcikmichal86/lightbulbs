from channels.generic.websocket import AsyncWebsocketConsumer
from myapi.models import Lightbulb, Blinds, Temperature
from myapi.serializers import DeviceSerializer, BlindsSerializer, TemperatureSerializer
import json
from channels.db import database_sync_to_async
from asyncio import sleep


class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        await self.accept()
        while True:
            await self.fetch_data()
            await sleep(0.5)


    async def fetch_data(self):
        message = await self.get_objects()
        await self.send(json.dumps(message))


    @database_sync_to_async
    def get_objects(self):
        devices = Lightbulb.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return serializer.data


class BlindsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        await self.accept()
        while True:
            await self.fetch_data()
            await sleep(0.5)


    async def fetch_data(self):
        message = await self.get_objects()
        await self.send(json.dumps(message))


    @database_sync_to_async
    def get_objects(self):
        devices = Blinds.objects.all()
        serializer = BlindsSerializer(devices, many=True)
        return serializer.data


class TemperatureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        await self.accept()
        while True:
            await self.fetch_data()
            await sleep(0.5)


    async def fetch_data(self):
        message = await self.get_objects()
        await self.send(json.dumps(message))




    @database_sync_to_async
    def get_objects(self):
        devices = Temperature.objects.all()
        serializer = TemperatureSerializer(devices, many=True)
        return serializer.data