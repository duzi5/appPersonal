from email.policy import default
from turtle import onkeypress
from flask import redirect, render_template, flash, url_for
from app import app, db, login_manager
from app.models.forms import formulario_login 
from app.models.tables import User
from flask_login import login_user


@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)  

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/login', methods=['GET' ,'POST'])
def login():
    form = formulario_login() 
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.usuario.data).first()
        if user and user.senha == form.senha.data:
            login_user(user)
            return redirect(url_for('index'))
        else: 
            flash('Login Inválido')
            return 'cai aqui2'
    return render_template('login.html', form = form)

@app.route('/teste/<info>')
@app.route('/teste', defaults = {'info':None})
def teste(info): 
   
    return "ok"
