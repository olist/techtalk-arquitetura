from rest_framework import serializers

from apps.matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id",
            "home_team_name",
            "home_team_score",
            "home_team_goals",
            "guest_team_name",
            "guest_team_score",
            "guest_team_goals",
        )
