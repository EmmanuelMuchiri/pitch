from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
from flask_uploads import UploadSet,configure_uploads,IMAGES


photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    # configure UploadSet
    configure_uploads(app,photos)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app