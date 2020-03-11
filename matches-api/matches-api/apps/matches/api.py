from rest_framework.viewsets import ModelViewSet

from apps.matches.models import Match
from apps.matches.serializers import MatchSerializer


class MatchViewSet(ModelViewSet):
    filterset_fields = ("home_team_name", "guest_team_name")
    ordering_fields = (
        "home_team_name",
        "home_team_score",
        "home_team_goals",
        "guest_team_name",
        "guest_team_score",
        "guest_team_goals",
    )
    search_fields = ("home_team_name", "guest_team_name")
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
