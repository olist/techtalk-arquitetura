import os
from pathlib import Path

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.db.backends.signals import connection_created
from django.dispatch import receiver

from utils import get_project_package

PROJECT_DIR = Path(__file__).absolute().parents[1]
PROJECT_PACKAGE = get_project_package(PROJECT_DIR)
DB_STATEMENT_TIMEOUT = 30_000

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{}.settings".format(PROJECT_PACKAGE))
_application = get_wsgi_application()

try:
    from whitenoise.django import DjangoWhiteNoise

    _application = DjangoWhiteNoise(_application)
except ImportError:
    pass


def application(environ, start_response):
    # Copy all QS_* wsgi environments to os.environ removing QS_ prefix
    # This is useful to use Apache SetEnv option to pass configuration
    # arguments to application.
    for envvar in environ:
        if envvar.startswith("QS_"):
            os.environ[envvar[3:]] = environ[envvar]

    return _application(environ, start_response)


@receiver(connection_created)
def setup_postgres(connection, **kwargs):
    if connection.vendor != "postgresql" or settings.DEBUG:
        return

    with connection.cursor() as cursor:
        cursor.execute(f"SET statement_timeout TO {DB_STATEMENT_TIMEOUT};")
