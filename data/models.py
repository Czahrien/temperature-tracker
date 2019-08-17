from django.db import models

class Email(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return '%s (%s)' % (self.email, self.name)

class MailingList(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    emails = models.ManyToManyField(Email,'emails')

    def get_emails(self):
        return [ x.email for x in self.emails.all() ]
    
    def __str__(self):
        return '%s' % (self.name)

class Device(models.Model):
    device = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.device)

class DataPoint(models.Model):
    date = models.DateTimeField()
    device = models.ForeignKey(Device, models.CASCADE, 'datapoints', to_field='device')

    def __str__(self):
        return '%s: %s' % (self.device, self.date)

    def save(self, *args, **kwargs):
        Device.objects.get_or_create(device=self.device, defaults={'description': 'Added automatically.'})
        super(DataPoint,self).save(*args, **kwargs)

class TemperatureDataPoint(DataPoint):
    temperature = models.IntegerField()
    crc_pass = models.BooleanField()
    raw_data = models.TextField()

    def __str__(self):
        return '%s %s %s' % (self.device, self.date, self.temperature)
