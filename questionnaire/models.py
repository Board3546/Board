import datetime

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models
from django.urls import reverse_lazy


class Service(models.Model):
    """Анкета"""

    SUBSCRIPTION_LEVEL = (
        (30, "TOP тариф"),
        (20, "VIP тариф"),
        (10, "Базовый тариф"),
    )
    SERVICE_TYPE = (
        ("", "выбрать..."),
        (1, "Девушка"),
        (2, "Массажистки"),
        (3, "Парни"),
        (4, "Фирма досуга"),
    )

    NATIONALITY = (
        ("", "выбрать..."),
        ("Русская/Русский", "Русская/Русский"),
        ("Украинка/Украинец", "Украинка/Украинец"),
        ("Негритянка/Негр", "Негритянка/Негр"),
        ("Мулатка/Мулат", "Мулатка/Мулат"),
        ("Азиатка/Азиат", "Азиатка/Азиат"),
        ("Кореянка/Кореец", "Кореянка/Кореец"),
        ("Татарка/Татар", "Татарка/Татар"),
        ("Казашка/Казах", "Казашка/Казах"),
        ("Узбечка/Узбек", "Узбечка/Узбек"),
    )

    GENDER = (
        ("", "выбрать..."),
        ("Натуралка/Натурал", "Натуралка/Натурал"),
        ("Лесби/Гей", "Лесби/Гей"),
        ("Би", "Би"),
    )

    APPEARANCE = (
        ("", "выбрать..."),
        ("Худая", "Худая"),
        ("Стройная", "Стройная"),
        ("Спортивная", "Спортивная"),
        ("Полная", "Полная"),
    )

    HAIR = (
        ("", "выбрать..."),
        ("Брюнетка", "Брюнетка"),
        ("Шатенка", "Шатенка"),
        ("Блондинка", "Блондинка"),
        ("Рыжая", "Рыжая"),
    )

    MESSANGERS = (
        ("", "выбрать..."),
        ("WhatsApp", "WhatsApp"),
        ("Viber", "Viber"),
        ("Telegram", "Telegram"),
    )
    title = models.CharField("Название", max_length=128)
    description = models.TextField(
        "Описание",
        validators=[
            MinLengthValidator(200, "Поле должно содержать минимум 200 символов")
        ],

    )
    age = models.SmallIntegerField("Возраст")
    weight = models.SmallIntegerField("Вес")
    height = models.SmallIntegerField("Рост")
    size = models.SmallIntegerField()
    hair = models.CharField(max_length=50, choices=HAIR)
    appearance = models.CharField("Телосложение", max_length=60, choices=APPEARANCE)
    nationality = models.CharField(max_length=60, choices=NATIONALITY)
    gender = models.CharField(max_length=60, choices=GENDER)
    is_published = models.BooleanField("Опубликовано", default=False)
    waiting_call = models.BooleanField("Жду звонка", default=False)
    subscription = models.IntegerField(choices=SUBSCRIPTION_LEVEL, default=10)
    confirmed = models.BooleanField("Фото подтверждено", default=False)
    views = models.IntegerField("Просмотры", default=0)
    location = models.CharField("Локация", max_length=50)
    phone = models.CharField("Номер телефона", max_length=20)
    messanger = models.CharField(
        "Привязанный мессенджер",
        choices=MESSANGERS,
        max_length=20,
        blank=True,
        null=True,
    )
    call_time_start = models.TimeField("Звонить с", default=datetime.time(0, 0))
    call_time_end = models.TimeField("Звонить до", default=datetime.time(23, 59))
    price_half_hour = models.IntegerField("Експресс (30 мин)", blank=True, null=True)
    price_one_hour = models.IntegerField("Цена час", blank=True, null=True)
    price_two_hours = models.IntegerField("Цена два часа", blank=True, null=True)
    price_full = models.IntegerField("Цена за ночь", blank=True, null=True)
    price_one_hour_outdoors = models.IntegerField(
        "Цена час на выезд", blank=True, null=True
    )
    price_two_hours_outdoors = models.IntegerField(
        "Цена два часа на выезд", blank=True, null=True
    )
    price_full_outdoors = models.IntegerField(
        "Цена за ночь на выезд", blank=True, null=True
    )
    additions = models.ManyToManyField("Addition", blank=True)
    owner = models.ForeignKey(
        "users.Profile",
        on_delete=models.PROTECT,
        related_name="services",
        verbose_name="Владелец анкеты",
    )
    type = models.SmallIntegerField("Тип анкеты", choices=SERVICE_TYPE)
    subscription_active = models.BooleanField(default=False)
    subscription_expire = models.DateTimeField(
        "Дата окончания подписки", blank=True, null=True
    )
    date_published = models.DateTimeField("Дата публикации", auto_now_add=True)
    on_top = models.DateTimeField("Поднять анкету", default=datetime.datetime.utcnow)
    video = models.FileField(
        upload_to="videos/%Y/%m/%d",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("service", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"
        ordering = ["-subscription", "-on_top"]


class MultipleImage(models.Model):
    """Модель, связанная с Анкетой, для добавления нескольких картинок на одну анкету"""

    service = models.ForeignKey(
        "Service", on_delete=models.PROTECT, related_name="images"
    )
    image = models.ImageField("Фото", upload_to="photos/%Y/%m/%d")
    moderated = models.BooleanField("Фото проверено", default=False)

    def __str__(self):
        return str(self.image)


class Addition(models.Model):
    """Дополнительные услуги в анкете"""

    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    title = models.CharField("Название услуги", max_length=60)
    price = models.IntegerField("Доплата за услугу", default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Категории дополнительных услуг"""

    title = models.CharField("Название категории", max_length=60)

    def __str__(self):
        return self.title


class Review(models.Model):
    """Отзывы к анкете"""

    user = models.CharField("Рецензент", max_length=128)
    date = models.DateTimeField("Дата публикации", auto_now_add=True)
    stars = models.SmallIntegerField("Оценка")
    message = models.TextField("Описание")
    moderated = models.BooleanField("Проверено", default=False)
    original_photo = models.BooleanField("Фото соответствует", blank=True, null=True)
    service = models.ForeignKey(
        "Service", on_delete=models.CASCADE, related_name="reviews"
    )


class OnTopPrice(models.Model):
    """Price for rising service on top of others"""

    price = models.IntegerField("Цена за поднятие анкеты", default=10)

    def save(self, *args, **kwargs):
        """One object only"""
        if not self.pk and OnTopPrice.objects.exists():
            raise ValidationError("There is can be only one OnTopPrice instance")
        return super(OnTopPrice, self).save(*args, **kwargs)

    def __str__(self):
        return (
            "Стоимость поднятия сейчас: "
            + str(self.price)
            + " руб. (нажмите, чтобы изменить)"
        )

    class Meta:
        verbose_name = "Стоимость Поднятия"
        verbose_name_plural = "Стоимость Поднятия"
