from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions
from .serializers import TemperatureDataPointSerializer
from .models import TemperatureDataPoint


class TemperatureDataPointViewset(viewsets.ModelViewSet):
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = TemperatureDataPoint.objects.all().order_by('date')
    serializer_class = TemperatureDataPointSerializer
