from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.PositiveIntegerField(unique=True, verbose_name='tg id', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
