from utils import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    senha= db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)