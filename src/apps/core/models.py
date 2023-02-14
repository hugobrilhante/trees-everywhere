from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(models.Model):
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"
        ordering = ("-created",)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    about = models.TextField(blank=True, null=True)
    accounts = models.ManyToManyField("Account", related_name="accounts", blank=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("-date_joined",)

    def __str__(self):
        return self.get_full_name()
