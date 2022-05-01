from email.policy import default
from turtle import onkeypress
from flask import redirect, render_template, flash, url_for
from app import app, db, login_manager
from app.models.forms import formulario_login 
from app.models.tables import User
from flask_login import login_user, logout_user



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
            flash('Logged in.')
            print('estou logado')
            user.is_autheticated = True
            return redirect(url_for('inicio'))
        else: 
            flash('Login Inválido')
            return redirect(url_for('login'))
    return render_template('login.html', form = form)

@app.route('/logout')
def logout(): 
    logout_user()
    flash("Logged out.")
    return redirect( url_for('index'))


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')