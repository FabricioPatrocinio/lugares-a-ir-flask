from flask import render_template, url_for, flash, request, redirect, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.model import db, Publicacao, Imagens, User, Estados, Cidades
from sqlalchemy.exc import IntegrityError
from . import bp_publicacoes
from datetime import date
import os
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename


# Caminho para o updload da imagem
UPLOAD_FOLDER = '/home/f/my-dev-py/lugares-a-ir/app/static/uploads/img/publicacoes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@bp_publicacoes.route('/', methods=['GET', 'POST'])
def index():
    title = 'Inicio publicações'

    user_id = current_user.id

    user = User.query.filter_by(id=user_id).first()

    return render_template('inicio.html', title=title, user=user)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

                if 'imagens[]' not in request.files:
                    flash('Nenhuma imagem selecionada. Por favor, selecione pelo menos uma imagem.', 'danger')
                    return redirect(request.url)

                files = request.files.getlist('imagens[]')
                filename = []

                for file in files:
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(UPLOAD_FOLDER, filename))

                publicacao = Publicacao(user.id, cidade, nome_local, descricao)
                
                for name in filename:
                    imagens = Imagens(publicacao.id, name)

                db.session.add(publicacao)
                db.session.add(imagens)
                db.session.commit()

                flash('Publicação adicionada com sucesso', 'success')
            else:
                flash('Você precisa preencher todos os dados.', 'danger')

        except IntegrityError:
            db.session.rollback()
            flash('Ocorreu algum erro inesperado.', 'danger')

    return render_template('add-publicacao.html', title=title, user=user, estado=estado)


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
