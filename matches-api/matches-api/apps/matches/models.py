from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

from utils import sns_publish


class Match(models.Model):
    home_team_name = models.CharField(max_length=64)
    home_team_goals = ArrayField(models.CharField(max_length=64), default=list, null=True, blank=True)
    guest_team_name = models.CharField(max_length=64)
    guest_team_goals = ArrayField(models.CharField(max_length=64), default=list, null=True, blank=True)

    class Meta:
        verbose_name = "match"
        verbose_name_plural = "matches"

    @property
    def home_team_score(self):
        return len(self.home_team_goals)

    @property
    def guest_team_score(self):
        return len(self.guest_team_goals)

    def save(self, *args, **kwargs):
        endpoint_url = settings.SNS_ENDPOINT_URL
        topic = settings.MATCH_CREATED_TOPIC_ARN if self.id is None else settings.MATCH_UPDATED_TOPIC_ARN
        dry_run = settings.SNS_DRY_RUN

        super().save(*args, **kwargs)

        data = self._serialize_data()
        sns_publish(endpoint_url, topic, data, dry_run)

    def _serialize_data(self):
        from apps.matches.serializers import MatchSerializer

        return MatchSerializer(self).data

    def __str__(self):
        return (
            f"{self.home_team_name} {self.home_team_score} x {self.guest_team_score} {self.guest_team_name}"
        )
