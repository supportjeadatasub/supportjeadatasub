from flask import Flask
from flask_cors import CORS
from models.user import db
from routes.auth import auth_bp
from routes.wallet import wallet_bp
from routes.general import general_bp

app = Flask(__name__)
# Allow any site (including your Netlify domain) to access /api/*
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SECRET_KEY'] = 'dev_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(wallet_bp, url_prefix='/api')
app.register_blueprint(general_bp, url_prefix='/api')

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
