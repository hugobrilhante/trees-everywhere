from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from src.apps.core.models import Account, PlantedTree, Tree, User


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_editable = ("active",)
    list_display = ("name", "active")
    list_filter = ("active",)
    search_fields = ("name",)


@admin.register(PlantedTree)
class PlantedTreeAdmin(ModelAdmin):
    list_display = ("tree", "user")
    search_fields = ("tree__name", "user__first_name", "user__last_name")


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "about", "accounts")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Tree)
class TreeAdmin(ModelAdmin):
    list_display = ("name", "scientific_name")
