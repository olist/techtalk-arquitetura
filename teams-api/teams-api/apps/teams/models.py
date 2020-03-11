from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    points = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"

    def __str__(self):
        return f"{self.name} {self.points}"
