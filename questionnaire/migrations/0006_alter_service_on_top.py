# Generated by Django 4.1.7 on 2023-03-28 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questionnaire", "0005_service_on_top"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="on_top",
            field=models.DateTimeField(
                default=datetime.datetime.utcnow, verbose_name="Поднять анкету"
            ),
        ),
    ]
