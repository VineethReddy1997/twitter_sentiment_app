from flask import Flask
from app.routes import main

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.register_blueprint(main)
    return app

app = create_app()
