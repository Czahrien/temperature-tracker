from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TemperatureDataPointSerializer
from .models import TemperatureDataPoint

class TemperatureDataPointViewset(viewsets.ModelViewSet):
    queryset = TemperatureDataPoint.objects.all().order_by('date')
    serializer_class = TemperatureDataPointSerializer
