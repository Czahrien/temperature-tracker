from django.db import models
from data.models import MailingList, Device, DataPoint


class AlertFamily(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    device = models.ForeignKey(Device, models.CASCADE, "alert_familys")
    mailing_lists = models.ManyToManyField(MailingList)

    def __str__(self):
        return '%s (%s)' % (self.name, self.device)

class AlertThreshold(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    family = models.ForeignKey(AlertFamily, models.CASCADE, 'thresholds')
    threshold_value = models.IntegerField()
    current_datapoint = models.ForeignKey(DataPoint, models.SET_NULL, null=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.family.name, self.name, self.threshold_value)
