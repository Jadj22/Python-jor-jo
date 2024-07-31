from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from .models import User

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

    def validate_username(self, username):
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
