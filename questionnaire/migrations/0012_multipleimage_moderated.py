# Generated by Django 4.1.7 on 2023-04-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questionnaire", "0011_alter_addition_price_alter_service_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="multipleimage",
            name="moderated",
            field=models.BooleanField(default=False, verbose_name="Модерация"),
        ),
    ]
