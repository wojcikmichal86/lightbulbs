from rest_framework import serializers
from .models import Lightbulb

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lightbulb
        fields = ('id','name', 'turned_on')
