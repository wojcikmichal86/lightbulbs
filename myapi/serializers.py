from rest_framework import serializers
from .models import Lightbulb, Blinds, Temperature

class LightbulbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lightbulb
        fields = ('id','name', 'turned_on')


class BlindsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blinds
        fields = ('id','name', 'closed')


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id','name', 'temperature')