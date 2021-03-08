from logging import NullHandler
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .model import configure as config_db, User


def create_app():
    app = Flask(__name__)

    app.secret_key = 'ursolobo'

    app.config['CACHE_TYPE'] = 'null'
    app.config['SECRET_KEY'] = 'ursolobo'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost:3306/lugares_a_ir'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    
    Migrate(app, app.db)
    
    login_manager =  LoginManager()
    login_manager.login_view = 'bp_auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()

    from .auth import bp_auth
    app.register_blueprint(bp_auth)

    from .publicacoes import bp_publicacoes
    app.register_blueprint(bp_publicacoes)

    return app
