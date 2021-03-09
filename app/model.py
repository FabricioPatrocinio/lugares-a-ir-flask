from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from datetime import datetime

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    img_perfil = db.Column(db.String(255), nullable=True)
    publicacao = db.relationship('Publicacao', backref='user')
    time_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __init__(self, nome, email, senha, img_perfil):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)
        self.img_perfil = img_perfil

    def verify_password(self, pwd):
        return check_password_hash(self.senha, pwd)


class Publicacao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    regiao = db.Column('Cidades', db.ForeignKey('cidades.id'))
    nome_local = db.Column(db.String(100), nullable=True)
    descricao = db.Column(db.String(2000))
    imagens = db.relationship('Imagens', backref='publicacao')
    time_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __init__(self, user_id, regiao, nome_local, descricao):
        self.user_id = user_id
        self.regiao = regiao
        self.nome_local = nome_local
        self.descricao = descricao


class Imagens(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publicacao_id = db.Column(db.Integer, db.ForeignKey('publicacao.id'))
    nome = db.Column(db.String(255), nullable=False)

    def __init__(self, publicacao_id, nome):
        self.publicacao_id = publicacao_id
        self.nome = nome


# Os estados e cidade você pode buscar SQLs completos na net
class Estados(db.Model):
    __tablename__ = 'estados'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(75), nullable=True)
    uf = db.Column(db.String(5), nullable=True)
    estado = db.relationship('Cidades', backref='estados')


class Cidades(db.Model):
    __tablename__ = 'cidades'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=True)
    id_estado = db.Column(db.Integer, db.ForeignKey('estados.id'))
    publicacao = db.relationship('Publicacao', backref='cidades')
