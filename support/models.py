from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars
from django.urls import reverse_lazy


# Create your models here.
class Support(models.Model):
    topic = models.CharField("Заголовок проблемы", max_length=200)
    slug = AutoSlugField(populate_from="topic", unique=True)
    description = models.TextField("Решение проблемы")

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse_lazy("topic", kwargs={"slug": self.slug})

    @property
    def short_description(self):
        return truncatechars(self.description, 35)

    class Meta:
        verbose_name = "Поддержка"
        verbose_name_plural = "Топики"
        ordering = ["topic"]


class Ticket(models.Model):
    TICKET_STATUS = (
        ("O", "open"),
        ("C", "closed"),
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Отправитель"
    )
    question = models.TextField("Вопрос")
    slug = AutoSlugField(populate_from="question", unique=True)
    answer = models.TextField("Ответ", blank=True, null=True)
    status = models.CharField(
        "Статус", choices=TICKET_STATUS, max_length=1, default="O"
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.question[:30] + "..." if len(self.question) > 30 else self.question

    def get_absolute_url(self):
        return reverse_lazy("ticket", kwargs={"slug": self.slug})

    @property
    def short_question(self):
        return truncatechars(self.question, 35)

    @property
    def short_answer(self):
        return truncatechars(self.answer, 35)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ["-status", "-created_at"]


class SiteReview(models.Model):
    rate = models.SmallIntegerField("Оценка")
    comment = models.TextField("Комментарий", null=True, blank=True)
    wishes = models.TextField("Пожелания", null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв о сайте"
        verbose_name_plural = "Отзывы о сайте"
        ordering = ["rate"]
