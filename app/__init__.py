from flask_api import FlaskAPI
from instance.config import Config
from app.models import db


def create_app():
    """
        Initialize Flask Api application
    """
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(Config())
    app.jinja_env.auto_reload = True
    app.conf = app.config
    db.init_app(app)
    with app.app_context():
        from .routes import book_bp
        from . import error_handler
        app.register_blueprint(book_bp)
    return app


app = create_app()
