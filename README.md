# CESI - Python - _Data Dragon_ de _League of Legends_

Dépôt Git créé durant le cours d'initiation à Python (dispensé du 04.05.2021 au 06.05.2021) de la formation de RIL DevOps du CESI. Application permettant le téléchargement du Data Dragon, dans sa globalité ou uniquement de la dernière version disponible. Permet également de mettre à jour une installation existante.

## Contenu du dépôt

Ce dépôt contient le projet personnel réalisé en Python, durant le cours d'initiation au langage. Ce dernier consiste à récupérer la dernière version du _Data Dragon_ (dossier .tgz ou .zip fourni par Riot Games) de _League of Legends_ et à mettre à jour le dépôt Git utilisé par mes différents projets avec la nouvelle version.

## Exécution du projet

Le projet nécessite quelques packages supplémentaires :

```bash
pip install requests
```

Dans certains cas, il peut être nécessaire d'installer une dépendance supplémentaire, qui est normalement intégrée à Python.

```bash
pip install tqdm
```

Une fois ces packages installés, il est nécessaire de se placer dans le dossier où se trouve les fichiers de l'application, puis de lancer la commande suivante : `python main.py`.