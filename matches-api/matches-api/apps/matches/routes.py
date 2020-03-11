from rest_framework.routers import SimpleRouter

from apps.matches.api import MatchViewSet

app_name = "matches"

router = SimpleRouter()
router.register(r"matches", MatchViewSet, basename="matches")

urlpatterns = router.urls
