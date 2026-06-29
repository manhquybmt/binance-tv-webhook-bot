from flask import Flask
from config import Config
from database import db

from dashboard.routes import dashboard_bp
from api.webhook import webhook_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(dashboard_bp)
app.register_blueprint(webhook_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
