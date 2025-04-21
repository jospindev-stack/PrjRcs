# API RESTful – Gestion des Commandes

Ce projet est une API RESTful développée en Python avec Flask pour permettre la gestion sécurisée des commandes via des opérations CRUD et une fonctionnalité de recherche. Ce projet a été réalisé dans un contexte pédagogique avec une authentification par jeton.

# Objectifs du projet

- Créer une API sécurisée permettant d’ajouter, consulter, modifier et supprimer des commandes
- Implémenter une recherche par nom de produit
- Restreindre l’accès aux fonctionnalités via un système d’authentification par jeton

# Technologies utilisées

- Flask
- Flask-RESTful
- Flask-SQLAlchemy (base de données SQLite)
- Flask-HTTPAuth (authentification par token)

# Structure du projet

- `app.py` : Script principal contenant les routes API et la configuration de Flask
- `test_orders_api.py` : Script de test pour simuler les appels API
- `instance/` : Contient la base SQLite et les configurations locales

# Fonctionnalités de l’API

## Authentification

- Token d'accès requis pour chaque requête
- Vérification automatique des droits d’accès

## Endpoints

- `PUT /order/<int:order_id>` : Ajouter une commande
  - Paramètres : `product_name`, `quantity`, `price`, `order_date`
- `GET /order/<int:order_id>` : Consulter une commande par ID
- `PATCH /order/<int:order_id>` : Modifier une commande
  - Paramètres partiels autorisés
- `DELETE /order/<int:order_id>` : Supprimer une commande
- `GET /ordersearch/<string:product_name>` : Rechercher une commande par nom

# Lancer l’API localement

1. Installer les dépendances :

```bash
pip install flask flask-restful flask-sqlalchemy flask-httpauth
```

2. Lancer l’application :

```bash
python app.py
```

3. Utiliser Postman ou curl pour tester les endpoints (avec token d’authentification).

# Auteur

Projet réalisé par BOMO MEKA JOSPIN MARIEL, dans le cadre du développement d’API sécurisée avec Flask.
