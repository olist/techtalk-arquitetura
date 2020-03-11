from loafer.managers import LoaferManager

from .routes import routes

manager = LoaferManager(routes=routes)
manager.run()
