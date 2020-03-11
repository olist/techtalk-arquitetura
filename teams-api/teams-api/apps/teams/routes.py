from rest_framework.routers import SimpleRouter

from apps.teams.api import TeamViewSet

app_name = "teams"

router = SimpleRouter()
router.register(r"teams", TeamViewSet, basename="teams")

urlpatterns = router.urls
