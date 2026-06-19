from flask import Flask, render_template, url_for, redirect, request
from utils import db
import os

# configurações para conexão do banco de dados
app = Flask(__name__)
app.config['SECRETY_KEY'] = os.getenv('SECRET_KEY')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('fases.tech')
db_database = os.getenv('DB_DATABASE')
db_port = os.getenv('DB_PORT')

conexao = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao

db.init_app(app)

# rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@app.route('/login')
def login():
    return render_template('login.html')