from flask import Flask
from routes.Bacteria_bp import BacteriaBP

app = Flask(__name__)

app.register_blueprint(BacteriaBP, url_prefix='/bacteria')

@app.route("/")
def Home():
    return "Hello Ziyad"