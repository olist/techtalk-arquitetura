from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=64, unique=True)
    position = models.CharField(max_length=64)
    goals = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"

    def __str__(self):
        return f"{self.name} {self.position} {self.goals}"
