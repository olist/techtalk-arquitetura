import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("home_team_name", models.CharField(max_length=64)),
                (
                    "home_team_goals",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                ("guest_team_name", models.CharField(max_length=64)),
                (
                    "guest_team_goals",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
            ],
            options={"verbose_name": "match", "verbose_name_plural": "matches",},
        ),
    ]
