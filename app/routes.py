"""Este módulo define as rotas da aplicação Flask."""
from app import app
from werkzeug.utils import redirect
from flask import render_template, request, flash

@app.route('/')
@app.route('/index', defaults={"nome": "usuario"})
@app.route('/index/<nome>/<profissao>/<canal>')
def index(nome, profissao, canal):
    """Renderiza a página inicial com nome, profissão e canal."""
    dados = {"profissao": profissao, "canal": canal}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    """Renderiza a página de contato."""
    return render_template('contato.html')

@app.route('/login')
def login():
    """Renderiza a página de login."""
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    """Autentica o usuário e redireciona conforme a validação."""
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == 'senha123':
        return f"usuario: {usuario} e senha: {senha}"
    else:
        flash("dados invalidos")
        return redirect('/login')
