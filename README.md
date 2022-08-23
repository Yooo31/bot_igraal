Dans la console aller dans le dossier :

# 1- Activer l'environement conda

conda activate bot_igraal

# 2- Lancer le terminal python

python3

# 3- Importer le script

from main import *

# API Start local

uvicorn main:app --reload