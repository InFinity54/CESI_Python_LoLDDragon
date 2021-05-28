import json
import os


# Récupère la version actuellement installée du Data Dragon.
# Renvoi le numéro de la version installée si existante, sinon renvoi False
def get_installed_ddragon_version(path):
    manifest_path = os.path.join(path, "lolpatch_latest/manifest.json")

    if os.path.exists(manifest_path):
        manifest = open(manifest_path, "r")
        manifest_json = json.loads(manifest.read())
        return manifest_json["v"]
    else:
        return False


# Détermine si le Data Dragon local doit être mis à jour.
# Renvoi le type de mise à jour disponible, ou False si aucune mise à jour n'est nécessaire.
def is_ddragon_needs_update(latest, current):
    latest_exploded = latest.split(".")
    current_exploded = current.split(".")

    if int(latest_exploded[0]) > int(current_exploded[0]):
        return "major"

    if int(latest_exploded[1]) > int(current_exploded[1]):
        return "minor"

    if int(latest_exploded[2]) > int(current_exploded[2]):
        return "patch"

    return False
