from django.db import models

class TemperatureDataPoint(models.Model):
    date = models.DateTimeField()
    device = models.CharField(max_length=30)
    temperature = models.IntegerField()
    crc_pass = models.BooleanField()
    raw_data = models.TextField()

    def __str__(self):
        return '%s %s %s' % (self.date, self.device, self.temperature)
