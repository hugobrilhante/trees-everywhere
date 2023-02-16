from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.core.views import PlantedTreeViewSet

router = DefaultRouter()
router.register(r"plantedtrees", PlantedTreeViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]
