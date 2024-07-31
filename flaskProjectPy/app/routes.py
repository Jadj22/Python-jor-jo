from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm
from .models import User
from . import db, bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))
            else:
                flash('Mot de passe incorrect', 'danger')
        else:
            flash('Nom d’utilisateur inexistant', 'danger')
    return render_template('login.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    users = User.query.all()
    return render_template('dashboard.html', users=users)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.", 'error')
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Compte créé avec succès !", 'success')
            return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@main.route('/help')
@login_required
def help():
    return render_template('help.html')
