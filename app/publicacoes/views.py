from flask import render_template, url_for, flash, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import exc, func
from . import bp_publicacoes
from app.model import db, User
from sqlalchemy.exc import IntegrityError
from datetime import date


@bp_publicacoes.route('/', methods=['GET', 'POST'])
def index():
    title = 'Inicio publicações'
    
    user_id = current_user.id
    
    user = User.query.filter_by(id=user_id).first()
    
    return render_template('inicio.html', title=title, user=user)


@bp_publicacoes.route('/add-publicacao/', methods=['GET', 'POST'])
def add_publicacao():
    title = 'Adicionar publicação'
    
    user_id = current_user.id
    
    user = User.query.filter_by(id=user_id).first()
    
    return render_template('add_publicacao.html', title=title, user=user)
