from django.conf import settings
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


class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    tree = models.ForeignKey("Tree", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=20, decimal_places=0)
    longitude = models.DecimalField(max_digits=20, decimal_places=0)

    class Meta:
        verbose_name = "planted tree"
        verbose_name_plural = "planted trees"
        ordering = ("-planted_at",)

    def __str__(self):
        return f"{self.tree} - age {self.age}"

    def location(self):
        """
        Returns the location of the planted tree
        """
        return self.latitude, self.longitude


class User(AbstractUser):
    about = models.TextField(blank=True, null=True)
    accounts = models.ManyToManyField("Account", related_name="accounts", blank=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("-date_joined",)

    def __str__(self):
        return self.get_full_name()


class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "tree"
        verbose_name_plural = "trees"

    def __str__(self):
        return f"{self.name}"
