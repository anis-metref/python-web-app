# python-web-app

# Application Flask pour la gestion des employés

Cette application Flask est un exemple simple qui permet de créer, modifier et supprimer des employés dans une base de données. Elle utilise une API Flask pour gérer les différentes opérations.

## Prérequis
-   Debian 11/12
-   Python 3.x installé sur votre machine
-   Git installé pour cloner le dépôt
-   python3-venv pour créer un environnement virtuel
-   python3-pip pour installer les paquets Python

## Installation

1.  Clonez ce dépôt en utilisant la commande suivante :
    
    
    

```
git clone https://github.com/anis-metref/python-web-app.git

```

-   Accédez au répertoire de l'application :
    
    
    

```cpp
cd Python-flask-App/flask_employee_app/

```

-   Créez un environnement virtuel pour isoler les dépendances de l'application :
    
    
    

```cpp
python3 -m venv venv

```

-   Activez l'environnement virtuel :
    -   Sur Linux/Mac :
        
        
        

```cpp
source venv/bin/activate

```

Sur Windows (PowerShell) :



```cpp
.\venv\Scripts\Activate.ps1

```

-   Installez les dépendances requises en exécutant la commande suivante :
    
    
    

```cpp
pip install -r requirements.txt

```

## Initialiser la base de donnés
Pour initialiser la base de données avec Flask-Migrate, vous devez exécuter les commandes suivantes :

1.  Initialisez la base de données :
    

    

```cpp
flask db init

```

-   Effectuez la première migration en spécifiant un message descriptif :
    
    

```cpp
flask db migrate -m "Migration initiale"

```

-   Mettez à jour la base de données avec les modifications apportées :
  

```cpp
flask db upgrade

```

Assurez-vous d'exécuter ces commandes dans votre environnement virtuel après avoir activé l'environnement virtuel avec la commande `source venv/bin/activate`.

## Utilisation

1.  Exécutez le fichier `manage.py` pour lancer l'application Flask :
    
    
    

```cpp
python manage.py

```

-   Ouvrez votre navigateur et accédez à l'adresse suivante :
    
    
    

```cpp
http://adresse_de_votre_serveur:5000

```

1.  Vous verrez l'interface de l'application qui vous permet de créer, modifier et supprimer des employés dans la base de données.

## Contributions

Les contributions à cette application sont les bienvenues ! Si vous trouvez des problèmes ou si vous avez des suggestions d'amélioration, n'hésitez pas à les signaler en créant une nouvelle issue ou en soumettant une pull request.
