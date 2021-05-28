import requests
import json


# Renvoi la liste de toutes les versions disponibles au téléchargement dans le Data Dragon.
def get_game_versions_list():
    # On initialise une liste de versions vide.
    versions = []

    # On récupère au format JSON la liste des versions disponibles.
    # On la converti directement en un dictionnaire avant de parser l'intégralité de la liste.
    for version in json.loads(requests.get("https://ddragon.leagueoflegends.com/api/versions.json").content):
        # On ajoute à notre liste de versions toutes celles ne commençant pas par "lolpatch" et par "0", qui ne sont
        # plus disponibles dans le Data Dragon.
        if version.startswith("lolpatch_") is False and version.startswith("0.") is False:
            # Pour la version 10.10, Riot avait tenté de modifier le fonctionnement du Data Dragon. On ne concerve donc
            # que les versions "normales" du Data Dragon, pour avoir le fonctionnement le plus commun possible.
            if version.startswith("10.10."):
                if len(version.split(".")[2]) == 1:
                    versions.append(version)
            else:
                versions.append(version)

    # On inverse l'ordre de la liste, pour organiser les versions de la plus ancienne à la plus récente.
    versions.reverse()
    return versions


# Renvoi le numéro de la dernière version du jeu disponible dans le Data Dragon.
def get_latest_game_version():
    versions = get_game_versions_list()
    return versions[len(versions) - 1]
