from flask import Flask
from flask_bootstrap import Bootstrap
from config import config


bootstrap = Bootstrap()

def create_app(config_name):
    fooleng = Flask(__name__)
    fooleng.config.from_object(config[config_name])
    config[config_name].init_app(fooleng)

    bootstrap.init_app(fooleng)

    from .tools import bsd as bsd_blueprint
    fooleng.register_blueprint(bsd_blueprint, url_prefix='/tools/BSD')

    return fooleng