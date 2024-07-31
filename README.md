Projet de Connexion, Inscription et Authentification des Utilisateurs

Ce projet est une application Python permettant la gestion de la connexion, de l'inscription et de l'authentification des utilisateurs. Il inclut les fonctionnalités suivantes :

- Inscription des utilisateurs avec vérification des données.
- Connexion des utilisateurs avec gestion des sessions.
- Authentification sécurisée avec hachage des mots de passe.

Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- pip (gestionnaire de paquets Python)
- PostgreSQL

Installation

Clonez le dépôt du projet depuis GitHub :

```bash
git clone https://github.com/Jadj22/Python-jor-jo.git
```

Accédez au répertoire du projet :

```bash
cd Python-jor-jo
```

Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

Configuration

Créez un fichier `.env` dans le répertoire racine du projet et ajoutez-y les variables d'environnement suivantes :

```
SECRET_KEY=votre_cle_secrete
DATABASE_URL=postgresql://votre_utilisateur:votre_mot_de_passe@localhost/votre_base_de_donnees
```

Création de la base de données

Assurez-vous d'avoir PostgreSQL installé et en cours d'exécution. Vous pouvez créer la base de données nécessaire avec les commandes suivantes :

Connectez-vous à PostgreSQL :

```bash
psql -U votre_utilisateur
```

Créez la base de données :

```sql
CREATE DATABASE votre_base_de_donnees;
```

Quittez PostgreSQL :

```sql
\q
```

Migration de la base de données

Appliquez les migrations pour créer les tables nécessaires dans la base de données :

```bash
flask db upgrade
```

Utilisation

Pour démarrer l'application, exécutez la commande suivante :

```bash
python app.py
```

Ouvrez votre navigateur et accédez à http://localhost:5000 pour voir l'application en action.

Fonctionnalités

Inscription

Les utilisateurs peuvent s'inscrire en fournissant un nom d'utilisateur, une adresse e-mail et un mot de passe. Les données sont vérifiées pour s'assurer qu'elles sont valides et uniques.

Connexion

Les utilisateurs inscrits peuvent se connecter en fournissant leur nom d'utilisateur et leur mot de passe. Une session est créée pour les utilisateurs authentifiés.

Authentification

Les mots de passe des utilisateurs sont hachés avant d'être stockés dans la base de données pour assurer la sécurité des informations sensibles.

Auteurs

Ce projet a été réalisé par :

- FOLLY jordan
- ADJANKE joel
