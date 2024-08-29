from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha-palavra-secreta"

# Importa as rotas após a criação do app
from app import routes