from rest_framework.viewsets import ModelViewSet

from apps.teams.models import Team
from apps.teams.serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    filterset_fields = ("name",)
    ordering_fields = ("name", "points", "matches", "wins", "draws", "losses", "goals", "goals_conceded")
    search_fields = ("name",)
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
