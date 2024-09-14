from flask import render_template, request, url_for, redirect, flash, session
from models.database import db, Game, Usuario, Imagem
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import Markup
import urllib
import json
import os
import uuid


@app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = Usuario.query.filter_by(email=email).first()

        #     if user and check_password_hash(user.password, password):
        #         session['user_id'] = user.id
        #         session['email'] = user.email
        #         nickname = user.email.split('@')
        #         flash(f'Login bem-sucedido! Bem-vindo {nickname[0]}!', 'success')
        #         return redirect(url_for('home'))
        #     else:
        #         flash('Falha no login. Verifique seu nome de usuário e senha.', 'danger')
        # return render_template('login.html')