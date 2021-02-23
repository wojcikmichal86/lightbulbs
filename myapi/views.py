from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DeviceSerializer
from .models import Lightbulb
from mysite.consumers import DeviceConsumer
import json

@api_view(['GET'])
def deviceList(request):
    devices = Lightbulb.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deviceDetail(request, pk):
    devices = Lightbulb.objects.get(id=pk)
    serializer = DeviceSerializer(devices, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def deviceCreate(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def deviceUpdate(request, pk):
    device = Lightbulb.objects.get(id=pk)
    serializer = DeviceSerializer(instance=device, data=request.data)
    if serializer.is_valid():
        serializer.save()
    #consumer = DeviceConsumer()
    #consumer.notify(serializer.data)
    return Response(serializer.data)


@api_view(['DELETE'])
def deviceDelete(request, pk):
    device = Lightbulb.objects.get(id=pk)
    device.delete()

    return Response('Deleted')




