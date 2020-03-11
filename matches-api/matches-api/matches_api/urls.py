from django.conf.urls import include, url

urlpatterns = [
    url(r"^v1/", include("apps.matches.routes")),
]
