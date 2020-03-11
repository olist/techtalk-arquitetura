import os


def when_ready(server):
    open("/tmp/app-initialized", "w").close()


bind = "unix:///tmp/nginx.socket"
max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS", "1000"))
max_requests_jitter = int(os.environ.get("GUNICORN_MAX_REQUESTS_JITTER", "25"))
