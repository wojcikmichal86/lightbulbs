from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LightbulbSerializer, BlindsSerializer, TemperatureSerializer
from .models import Lightbulb, Blinds, Temperature


@api_view(['GET'])
def LightbulbList(request):
    devices = Lightbulb.objects.all() #gets all the objects from the Lightbulb model
    serializer = LightbulbSerializer(devices, many=True) #turns the data from the model to json
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['GET'])
def LightbulbDetail(request, pk):
    devices = Lightbulb.objects.get(id=pk) #gets an object from the Lightbulb model by id
    serializer = LightbulbSerializer(devices, many=False) #turns the data from the model to json
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['POST'])
def LightbulbCreate(request):
    serializer = LightbulbSerializer(data=request.data) #turns the data from the request to json
    if serializer.is_valid(): #validates the data from the request
        serializer.save() #saves the object in the DB with the request json data
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['PUT'])
def LightbulbUpdate(request, pk):
    device = Lightbulb.objects.get(id=pk) #gets an object from the Lightbulb model by id
    serializer = LightbulbSerializer(instance=device, data=request.data) #turns the data from the request to json
    if serializer.is_valid(): #validates the data from the request
        serializer.save() #saves the object in the DB with the request json data
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['DELETE'])
def LightbulbDelete(request, pk):
    device = Lightbulb.objects.get(id=pk) #gets an object from the Lightbulb model by id
    device.delete() # removes the object from the DB
    return Response('Deleted') #sends the string as a response to the request (no json is sent)


@api_view(['GET'])
def BlindsList(request):
    devices = Blinds.objects.all() #gets all the objects from the Blinds model
    serializer = BlindsSerializer(devices, many=True) #turns the data from the model to json
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['GET'])
def BlindsDetail(request, pk):
    devices = Blinds.objects.get(id=pk) #gets an object from the Blinds model by id
    serializer = BlindsSerializer(devices, many=False) #turns the data from the model to json
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['POST'])
def BlindsCreate(request):
    serializer = BlindsSerializer(data=request.data) #turns the data from the request to json
    if serializer.is_valid(): #validates the data from the request
        serializer.save() #saves the object in the DB with the request json data
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['PUT'])
def BlindsUpdate(request, pk):
    device = Blinds.objects.get(id=pk) #gets an object from the Blinds model by id
    serializer = BlindsSerializer(instance=device, data=request.data) #turns the data from the request to json
    if serializer.is_valid(): #validates the data from the request
        serializer.save() #saves the object in the DB with the request json data
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['DELETE'])
def BlindsDelete(request, pk):
    device = Blinds.objects.get(id=pk) #gets an object from the Blinds model by id
    device.delete() # removes the object from the DB
    return Response('Deleted') #sends the string as a response to the request (no json is sent)


@api_view(['GET'])
def TemperatureList(request):
    devices = Temperature.objects.all() #gets all the objects from the Temperature model
    serializer = TemperatureSerializer(devices, many=True) #turns the data from the model to json
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['GET'])
def TemperatureDetail(request, pk):
    devices = Temperature.objects.get(id=pk) #gets an object from the Temperature model by id
    serializer = TemperatureSerializer(devices, many=False) #turns the data from the model to json
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['POST'])
def TemperatureCreate(request):
    serializer = TemperatureSerializer(data=request.data) #turns the data from the request to json
    if serializer.is_valid(): #validates the data from the request
        serializer.save() #saves the object in the DB with the request json data
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['PUT'])
def TemperatureUpdate(request, pk):
    device = Temperature.objects.get(id=pk) #gets an object from the Temperature model by id
    serializer = TemperatureSerializer(instance=device, data=request.data) #turns the data from the request to json
    if serializer.is_valid(): #validates the data from the request
        serializer.save() #saves the object in the DB with the request json data
    return Response(serializer.data) #sends the json as a respons to the request


@api_view(['DELETE'])
def TemperatureDelete(request, pk):
    device = Temperature.objects.get(id=pk) #gets an object from the Temperature model by id
    device.delete() # removes the object from the DB
    return Response('Deleted') #sends the string as a response to the request (no json is sent)s




