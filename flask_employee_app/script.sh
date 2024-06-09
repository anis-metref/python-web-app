# Initialiser la base de données
sudo flask db init || true
sudo flask db migrate -m "Migration initiale"
sudo flask db upgrade

# Lancer l'application Flask
#python3 manage.py
