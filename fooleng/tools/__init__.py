from flask import Blueprint

bsd = Blueprint('BSD', __name__)

from . import views
