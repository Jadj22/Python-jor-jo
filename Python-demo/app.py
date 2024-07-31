from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from flask_bcrypt import Bcrypt
from config import Config
from config import DevelopmentConfig, ProductionConfig
import os

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app = Flask(__name__)
app.config.from_object(Config)

if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(
        'Nom d’utilisateur',
        validators=[
            InputRequired(message="Ce champ est requis"),
            Length(min=4, max=20, message="Le nom d'utilisateur doit contenir entre 4 et 20 caractères")
        ],
        render_kw={"placeholder": "Nom d'utilisateur"}
    )

    password = PasswordField(
        'Mot de passe',
        validators=[
            InputRequired(message="Ce champ est requis"),
            Length(min=8, max=20, message="Le mot de passe doit contenir entre 8 et 20 caractères")
        ],
        render_kw={"placeholder": "Mot de passe"}
    )

    confirm_password = PasswordField(
        'Confirmer le mot de passe',
        validators=[
            InputRequired(message="Ce champ est requis"),
            EqualTo('password', message='Les mots de passe doivent correspondre')
        ],
        render_kw={"placeholder": "Confirmer le mot de passe"}
    )

    submit = SubmitField('S’inscrire')

    @staticmethod
    def validate_username(username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")


class LoginForm(FlaskForm):
    username = StringField(
        'Nom d’utilisateur',
        validators=[
            InputRequired(message="Ce champ est requis"),
            Length(min=4, max=20, message="Le nom d'utilisateur doit contenir entre 4 et 20 caractères")
        ],
        render_kw={"placeholder": "Nom d'utilisateur"}
    )

    password = PasswordField(
        'Mot de passe',
        validators=[
            InputRequired(message="Ce champ est requis"),
            Length(min=8, max=20, message="Le mot de passe doit contenir entre 8 et 20 caractères")
        ],
        render_kw={"placeholder": "Mot de passe"}
    )

    submit = SubmitField('Connexion')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    users = User.query.all()  # Obtenir tous les utilisateurs
    return render_template('dashboard.html', users=users)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.", 'error')
        else:
            # Créer un nouvel utilisateur
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Compte créé avec succès !", 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')


@app.route('/help')
@login_required
def help():
    return render_template('help.html')


if __name__ == "__main__":
    app.run(debug=True)
