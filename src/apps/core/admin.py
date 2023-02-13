from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.apps.core.models import Account


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_editable = ("active",)
    list_display = ("name", "active")
    list_filter = ("active",)
    search_fields = ("name",)
