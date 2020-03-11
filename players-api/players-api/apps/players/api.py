from rest_framework.viewsets import ModelViewSet

from apps.players.models import Player
from apps.players.serializers import PlayerSerializer


class PlayerViewSet(ModelViewSet):
    filterset_fields = ("name", "position")
    ordering_fields = ("name", "position", "goals")
    search_fields = ("name", "position")
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
