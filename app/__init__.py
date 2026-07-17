from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    from app.routes.api import api_bp
    app.register_blueprint(api_bp)

    from app.routes.scene import scene_bp
    app.register_blueprint(scene_bp)

    from app.routes.image import image_bp
    app.register_blueprint(image_bp)

    from app.routes.voice import voice_bp
    app.register_blueprint(voice_bp)
    
    from app.routes.video import video_bp
    app.register_blueprint(video_bp)
    
    return app