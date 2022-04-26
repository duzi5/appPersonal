from email.policy import default
from mailbox import NotEmptyError
from app import db
from datetime import datetime

class User(db.Model): 
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True )
    senha = db.Column(db.String)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    tipo = db.Column(db.Boolean)
    ativo = db.Column(db.Boolean)
    altura = db.Column(db.Integer)
    peso = db.Column(db.Integer)
    problemasCardiacos = db.Column(db.Boolean)
    problemasOsseos = db.Column(db.Boolean)
    objetivo = db.Column(db.SmallInteger)
    detalhesProblemas = db.Column(db.String)
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
    user_id = db.Column(db.ForeignKey('users.id'))
    personal_id = db.Column(db.ForeignKey('personais.id'))
    exercicios = db.column(db.String)
    user = db.relationship('User', foreign_key = user_id)

    def __init__(self, data, user_id, personal_id, exercicios):
        self.data = data
        self.user_id = user_id
        self.personal_id = personal_id



class Personal(db.Model): 
    __tablename__ = "personais"
    
    id = db.Column(db.Integer, primary_key =  True)
    nome = db.Column(db.Integer)
    data_inscricao = db.Column(db.DateTime, nullable = False)
    email = db.Column(db.String*(120))
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

