
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