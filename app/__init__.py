from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
