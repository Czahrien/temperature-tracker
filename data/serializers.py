from .models import TemperatureDataPoint
from rest_framework import serializers


class TemperatureDataPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureDataPoint
        fields = ['date', 'device', 'temperature', 'crc_pass', 'raw_data']
