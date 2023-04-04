# Generated by Django 4.0.6 on 2022-10-02 10:28

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200, verbose_name='Заголовок проблемы')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='topic', unique=True)),
                ('description', models.TextField(verbose_name='Решение проблемы')),
            ],
            options={
                'verbose_name': 'Поддержка',
                'verbose_name_plural': 'Поддержки',
                'ordering': ['topic'],
            },
        ),
    ]