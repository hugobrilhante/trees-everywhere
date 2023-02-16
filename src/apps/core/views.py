from rest_framework import viewsets

from .models import PlantedTree
from .serializers import PlantedTreeSerializer


class PlantedTreeViewSet(viewsets.ModelViewSet):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantedTreeSerializer

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)
