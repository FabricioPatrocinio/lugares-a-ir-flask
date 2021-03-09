from flask import render_template, url_for, flash, request, redirect, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from . import bp_publicacoes
from app.model import db, User, Estados, Cidades
from sqlalchemy.exc import IntegrityError
from datetime import date
import os
from flask_dropzone import Dropzone


# Caminho para o updload da imagem
IMAGE_UPLOADS = '/home/f/my-dev-py/lugares-a-ir/app/static/uploads/img/perfil'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


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

    # Estados, nao passados em json
    estado = Estados.query.all()

    if request.method == 'POST':
        cidade = request.form['cidade']
        nome_local = request.form['nome_local']
        descricao = request.form['descricao']

        try:
            if cidade != '' and nome_local != '' and descricao != '':

                if request.files:
                    ...
            else:
                flash('Você precisa preencher todos os dados.')

        except IntegrityError:
            db.session.rollback()
            flash('Ocorreu algum erro inesperado.', 'danger')

    return render_template('add_publicacao.html', title=title, user=user, estado=estado)


@bp_publicacoes.route('/add-publicacao/cidade/<id_estado>')
def cidade(id_estado):
    cidade = Cidades.query.filter_by(id_estado=id_estado).all()
    cidadeArray = []

    for cidade in cidade:
        cidadeObj = {}
        cidadeObj['id'] = cidade.id
        cidadeObj['nome'] = cidade.nome
        cidadeArray.append(cidadeObj)

    return jsonify({'cidadearray': cidadeArray})
