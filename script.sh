# Initialiser la base de données
flask db init || true
flask db migrate -m "Migration initiale"
flask db upgrade

# Lancer l'application Flask
python3 manage.py
