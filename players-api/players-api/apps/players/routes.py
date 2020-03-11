from rest_framework.routers import SimpleRouter

from apps.players.api import PlayerViewSet

app_name = "players"

router = SimpleRouter()
router.register(r"players", PlayerViewSet, basename="players")

urlpatterns = router.urls
