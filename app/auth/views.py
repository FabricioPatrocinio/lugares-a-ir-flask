from flask import render_template, url_for, flash, request, redirect, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from app.model import db, User, Estados, Cidades
from . import bp_auth
from werkzeug.utils import secure_filename
import os

# Caminho para o updload da imagem
IMAGE_UPLOADS = '/home/f/my-dev-py/lugares-a-ir/app/static/uploads/img/perfil'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'
    nome = ''

    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        try:
            user = User.query.filter_by(nome=nome).first()

            if not user or not user.verify_password(senha):
                if not user:
                    flash('Seu nome de usuário não existe ou está incorreto.', 'danger')

                if user and not user.verify_password(senha):
                    flash(
                        'Sua senha está incorreta, por favor tente novamente.', 'danger')

                return redirect(url_for('bp_auth.login'))

            login_user(user)
            return redirect(url_for('bp_publicacoes.index'))
        except IntegrityError:
            db.session.rollback()
            flash('Ocorreu algum erro inesperado.', 'danger')

    return render_template('login.html', title=title)


# Desfazer login e retorna a page login
@bp_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()

    return redirect(url_for('bp_auth.login'))


# Função que verifica se é do tipo imagem
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp_auth.route('/criar-conta/', methods=['GET', 'POST'])
def criar_conta():
    title = 'Criar conta'

    # Estados, nao passados em json
    estado = Estados.query.all()

    if request.method == 'POST':
        nome = request.form['nome']
        regiao = request.form['cidade']
        email = request.form['email']
        senha = request.form['senha']
        conf_senha = request.form['conf_senha']

        try:
            if nome != '' and regiao != '' and email != '' and senha != '':

                if request.files:
                    imagem = request.files['img_perfil']

                    if imagem.filename != '':

                        if not allowed_file(imagem.filename):
                            flash(
                                'O arquivo precisa ser imagem do tipo PNG, JPG, JPEG ou GIF', 'danger')

                        filename = secure_filename(imagem.filename)

                        imagem.save(os.path.join(
                            IMAGE_UPLOADS, filename))
                        img_perfil = filename

                        if conf_senha == senha:
                            conta = User(nome, regiao, email,
                                         senha, img_perfil)
                            db.session.add(conta)
                            db.session.commit()

                            flash('Sua conta foi criado com sucesso!', 'success')
                        else:
                            flash(
                                'Suas senhas não coincidem, por favor crie sua senha e confirme-a.', 'danger')
            else:
                flash('Você precisa preencher todos os dados.', 'danger')

        except IntegrityError:
            db.session.rollback()
            flash('Seu email ou nome de usuário já estão em uso, por favor tente novamente usando outro email ou nome de usuário', 'danger')

    return render_template('criar-conta.html', title=title, estado=estado)


@bp_auth.route('/criar-conta/cidade/<id_estado>')
def cidade(id_estado):
    cidade = Cidades.query.filter_by(id_estado=id_estado).all()
    cidadeArray = []

    for cidade in cidade:
        cidadeObj = {}
        cidadeObj['id'] = cidade.id
        cidadeObj['nome'] = cidade.nome
        cidadeArray.append(cidadeObj)

    return jsonify({'cidadearray': cidadeArray})


@bp_auth.route('/perfil', methods=['GET', 'POST'])
def perfil():
    title = 'Perfil'

    user_id = current_user.id

    user = User.query.filter_by(id=user_id).first()

    return render_template('perfil.html', title=title, user=user)
