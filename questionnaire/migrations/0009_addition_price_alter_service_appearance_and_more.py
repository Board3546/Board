# Generated by Django 4.1.7 on 2023-03-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "questionnaire",
            "0008_alter_ontopprice_options_service_call_time_end_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="addition",
            name="price",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Доплата за услугу"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="appearance",
            field=models.CharField(
                choices=[
                    ("Худая", "Худая"),
                    ("Стройная", "Стройная"),
                    ("Спортивная", "Спортивная"),
                    ("Полная", "Полная"),
                ],
                max_length=60,
                verbose_name="Телосложение",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="gender",
            field=models.CharField(
                choices=[
                    ("Натуралка/Натурал", "Натуралка/Натурал"),
                    ("Лесби/Гей", "Лесби/Гей"),
                    ("Би", "Би"),
                ],
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="nationality",
            field=models.CharField(
                choices=[
                    ("Русская/Русский", "Русская/Русский"),
                    ("Украинка/Украинец", "Украинка/Украинец"),
                    ("Негритянка/Негр", "Негритянка/Негр"),
                    ("Мулатка/Мулат", "Мулатка/Мулат"),
                    ("Азиатка/Азиат", "Азиатка/Азиат"),
                    ("Кореянка/Кореец", "Кореянка/Кореец"),
                    ("Татарка/Татар", "Татарка/Татар"),
                    ("Казашка/Казах", "Казашка/Казах"),
                    ("Узбечка/Узбек", "Узбечка/Узбек"),
                ],
                max_length=60,
            ),
        ),
    ]