# Generated by Django 2.2.4 on 2019-08-17 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0003_auto_20190817_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Device')),
            ],
        ),
        migrations.CreateModel(
            name='AlertThreshold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('threshold_value', models.IntegerField()),
                ('current_data_point', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.DataPoint')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thresholds', to='data_alerts.AlertFamily')),
            ],
        ),
    ]