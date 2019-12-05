# Generated by Django 2.2.4 on 2019-08-17 17:03

from django.db import migrations, models
import django.db.models.deletion
from data.models import TemperatureDataPoint, DataPoint


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    def createDataPoints(apps, schema_editor):
        old_TemperatureDataPoint = apps.get_model("data", "TemperatureDataPoint")
        old_tdps = old_TemperatureDataPoint.objects.all();
        DataPoint.objects.bulk_create([
            DataPoint(id=x.id, date=x.date, device=x.device) for x in old_TemperatureDataPoint.objects.all()
        ])
    
    def createDataPointReferences(apps, schema_editor):
        for t in TemperatureDataPoint.objects.all():
            t.datapoint_ptr = DataPoint.objects.get(id=t.id)
            t.save()


    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('device', models.CharField(max_length=30)),
            ],
        ),
        migrations.RunPython(createDataPoints),
        migrations.RemoveField(
            model_name='temperaturedatapoint',
            name='date',
        ),
        migrations.RemoveField(
            model_name='temperaturedatapoint',
            name='device',
        ),
        migrations.AddField(
            model_name='temperaturedatapoint',
            name='datapoint_ptr',
            field=models.OneToOneField(auto_created=True, null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.DataPoint'),
            preserve_default=False,
        ),
        migrations.RunPython(createDataPointReferences),
        migrations.RemoveField(
            model_name='temperaturedatapoint',
            name='id',
        ),
    ]