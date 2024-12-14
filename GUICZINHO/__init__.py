<<<<<<< HEAD

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "cavalo_de_troia"

app.config['SQLACHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/GUIC'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


banco_dados= SQLAlchemy(app)

from GUICZINHO import models, routes

with app.app_context():
    banco_dados.cretae_all() # CRIAR AS TABELAS
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

banco_dados = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações do aplicativo
    app.config['SECRET_KEY'] = "cavalo_de_troia"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/GUIC'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com o app
    banco_dados.init_app(app)

    # Criação das tabelas no banco (dentro do contexto da aplicação)
    with app.app_context():
        banco_dados.create_all()

    return app
>>>>>>> 6077cfe (quinto commit)
