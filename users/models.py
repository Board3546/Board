from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, primary_key=True, related_name="profile"
    )
    balance = models.IntegerField(default=0)
    phone = models.CharField("Телефон", max_length=20)
    favorites = models.ManyToManyField(
        "questionnaire.Service", verbose_name="Избранное", blank=True
    )

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return
