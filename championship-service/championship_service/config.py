from prettyconf import config


class Settings:
    LOG_LEVEL = config("LOG_LEVEL", default="INFO")
    LOGGERS = config("LOGGERS", default="", cast=config.list)

    WAIT_TIME_SECONDS = config("WAIT_TIME_SECONDS", default="5", cast=config.eval)

    AWS_DEFAULT_REGION = config("AWS_DEFAULT_REGION")
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_ENDPOINT_URL = config("AWS_ENDPOINT_URL", default=None)

    TEAMS_MATCH_CREATED_QUEUE = config("TEAMS_MATCH_CREATED_QUEUE")
    PLAYERS_MATCH_CREATED_QUEUE = config("PLAYERS_MATCH_CREATED_QUEUE")

    TEAMS_API_URL = config("TEAMS_API_URL")
    PLAYERS_API_URL = config("PLAYERS_API_URL")


settings = Settings()
