from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin



app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)


login_manager = LoginManager()
login_manager.init_app(app)



from app.controllers import default
from app.models import tables, forms 
from app.models.tables import User, UserMixin

