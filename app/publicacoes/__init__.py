from flask import Blueprint

bp_publicacoes = Blueprint('bp_publicacoes', __name__,
                           static_folder='static', template_folder='templates')

from . import views
