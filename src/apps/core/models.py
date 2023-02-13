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
