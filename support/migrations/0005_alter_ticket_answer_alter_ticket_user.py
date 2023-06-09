# Generated by Django 4.0.6 on 2022-10-05 17:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0004_ticket_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
    ]
