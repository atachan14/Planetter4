from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

from routes.index import index_bp
from routes.auth import auth_bp
from routes.partial import partial_bp

app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(partial_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
