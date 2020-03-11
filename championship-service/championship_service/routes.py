from loafer.ext.aws.routes import SNSQueueRoute

from .config import settings
from .handlers import PlayerHandler, TeamHandler, error_handler

provider_options = {
    "endpoint_url": settings.AWS_ENDPOINT_URL,
    "options": {"MaxNumberOfMessages": 10, "WaitTimeSeconds": settings.WAIT_TIME_SECONDS},
}


routes = (
    SNSQueueRoute(
        settings.TEAMS_MATCH_CREATED_QUEUE,
        provider_options=provider_options,
        handler=TeamHandler(),
        error_handler=error_handler,
    ),
    SNSQueueRoute(
        settings.PLAYERS_MATCH_CREATED_QUEUE,
        provider_options=provider_options,
        handler=PlayerHandler(),
        error_handler=error_handler,
    ),
)
