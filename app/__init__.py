from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.main.routes import main
    from app.visualisations.routes import viz

    app.register_blueprint(main)
    app.register_blueprint(viz)

    return app

