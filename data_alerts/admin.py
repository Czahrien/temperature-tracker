from django.contrib import admin
from .models import AlertFamily, AlertThreshold

admin.site.register(AlertFamily)
admin.site.register(AlertThreshold)