# Generated by Django 2.2.4 on 2019-08-17 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertfamily',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alert_familys', to='data.Device'),
        ),
    ]