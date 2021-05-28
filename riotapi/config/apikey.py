import os
from lolddragon.assets.colors.fore import ForeColor
from lolddragon.assets.font import FontStyle


# Retourne la clé à utiliser pour utiliser les API de Riot Games, depuis le fichier de configuration dédié
def get_riot_api_key():
    file_path = os.path.join(os.path.abspath(os.getcwd()), "config/apikey.txt")
    
    if os.path.exists(file_path):
        apikey_file = open(file_path, "r")
        apikey_file_lines = apikey_file.readlines()

        if len(apikey_file_lines) > 0:
            apikey = apikey_file_lines[0]

            if (apikey.startswith("RGAPI-")):
                return apikey
            else:
                print(ForeColor.Yellow + "Clé d'API Riot Games incorrecte." + FontStyle.Normal)
        else:
            print(ForeColor.Red + "Aucune clé d'API Riot Games renseignée." + FontStyle.Normal)
    else:
        print(ForeColor.Red + "Fichier de configuration de la clé d'API Riot Games introuvable." + FontStyle.Normal)

    return False
