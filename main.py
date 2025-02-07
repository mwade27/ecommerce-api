from flask import Flask
from app.config import Config
from app.db import db
from app.routes.auth import auth_bp
from app import create_app

app = create_app()



app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)