import os
from flask import Flask, current_app
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

