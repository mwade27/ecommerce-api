from flask import Flask
from flask_bcrypt import Bcrypt
from .config import Config
from .routes.auth import auth_bp  # Import your blueprint

bcrypt = Bcrypt()  # Create the Bcrypt instance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load the config

    bcrypt.init_app(app)  # Initialize bcrypt with the app

    app.register_blueprint(auth_bp)  # Register the auth blueprint
    return app