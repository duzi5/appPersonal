from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///storage.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

DEBUG = True

SECRET_KEY = 'uma-chave-bem-legal'