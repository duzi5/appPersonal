from email.policy import default
from mailbox import NotEmptyError
from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id = user_id)



class User(db.Model, UserMixin): 
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True )
    senha = db.Column(db.String)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    dataDeInscricao= db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __init__(self, username, senha, nome, email):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.email = email

    def __repr__(self): 
        return "<User %r>" % self.username



class Treino(db.Model): 
    __tablename__ = "treinos"
    id = db.Column(db.Integer, primary_key =  True)
    data = db.Column(db.DateTime, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    personal_id = db.Column(db.ForeignKey('personais.id'))
    exercicios = db.Column(db.String)
   

    def __init__(self, data, user_id, personal_id, exercicios):
        self.data = data
        self.user_id = user_id
        self.personal_id = personal_id
        self.exercicios = exercicios    
    def __repr__(self, id):
        return " treino %r " % self.id



class Personal(db.Model): 
    __tablename__ = "personais"
    
    id = db.Column(db.Integer, primary_key =  True)
    nome = db.Column(db.Integer)
    data_inscricao = db.Column(db.DateTime, nullable = False)
    email = db.Column(db.String(120))
    senha = db.Column(db.String(120))
    alunos = db.Column(db.String)
    ativo = db.Column(db.Boolean)
    
    def __init__(self, nome, data_incricao, email, senha, ativo, alunos):
        self.data_inscricao = data_incricao
        self.nome = nome
        self.email = email
        self.senha = senha
        self.alunos = alunos
        self.ativo = ativo

    def __repr__(self):
        return "Personal %r" % self.nome

