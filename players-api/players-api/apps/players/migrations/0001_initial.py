from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                ("position", models.CharField(max_length=64)),
                ("goals", models.PositiveIntegerField(default=0)),
            ],
            options={"verbose_name": "player", "verbose_name_plural": "players",},
        ),
    ]
