# Generated by Django 4.1.7 on 2023-03-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questionnaire", "0006_alter_service_on_top"),
    ]

    operations = [
        migrations.CreateModel(
            name="OnTopPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        default=10, verbose_name="Цена за поднятие анкеты"
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ["-subscription", "-on_top"],
                "verbose_name": "Анкета",
                "verbose_name_plural": "Анкеты",
            },
        ),
    ]
