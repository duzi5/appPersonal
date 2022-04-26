from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = "sqlite:///storage.db"
db = SQLAlchemy(app)



from app.controllers import default
