from django.contrib import admin
from .models import Email, MailingList, Device, DataPoint, TemperatureDataPoint

admin.site.register(Device)
admin.site.register(DataPoint)
admin.site.register(TemperatureDataPoint)
admin.site.register(Email)
admin.site.register(MailingList)