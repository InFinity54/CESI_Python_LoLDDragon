from lolddragon.assets.colors.fore import ForeColor
from lolddragon.assets.font import FontStyle
from lolddragon.ddragon.install import fresh_ddragon_install_all, fresh_ddragon_install_latest
from lolddragon.ddragon.update import update_ddragon
from lolddragon.ddragon.versions import get_installed_ddragon_version, is_ddragon_needs_update
from lolddragon.riotapi.config.apikey import get_riot_api_key
from lolddragon.riotapi.config.ddragonfolder import get_ddragon_folder
from lolddragon.riotapi.lol.versions import get_latest_game_version

# Récupération de la clé d'API Riot
from lolddragon.system.console import clear_console

riot_apikey = get_riot_api_key()
if riot_apikey is not False:
    print("Clé pour API Riot Games :", riot_apikey)

# Récupération de l'emplacement du dossier
ddragon_path = get_ddragon_folder()
if ddragon_path is not False:
    print("Chemin d'accès au Data Dragon :", ddragon_path)

# Récupération de la dernière version disponible dans le Data Dragon
latest_version = get_latest_game_version()
if latest_version is not False:
    print("Dernier patch de League of Legends :", latest_version)

# Récupération de la version installée du Data Dragon
installed_version = get_installed_ddragon_version(ddragon_path)
if installed_version is not False:
    print("Version actuelle du Data Dragon :", installed_version)

# Si les informations nécessaires au fonctionnement du programme ont été correctement récupérées, on procède à la
# recherche de mise à jour.
if ddragon_path is not False and latest_version is not False:
    # Si on a une version installée du Data Dragon, on vérifie si elle doit être mise à jour ou non.
    if installed_version is not False:
        needs_update = is_ddragon_needs_update(latest_version, installed_version)

        if needs_update is False:
            # Aucune mise à jour à faire, on arrête le programme ici.
            print(ForeColor.Green + "Le Data Dragon est à jour." + FontStyle.Normal)
        else:
            # On a une mise à jour à faire, on prévient l'utilisateur du type de mise à jour à réaliser.
            if needs_update == "major":
                print(ForeColor.Yellow + "Une nouvelle saison de League of Legends est disponible dans le Data Dragon.",
                      FontStyle.Normal)
            elif needs_update == "minor":
                print(ForeColor.Yellow + "Un nouveau patch de League of Legends est disponible dans le Data Dragon.",
                      FontStyle.Normal)
            elif needs_update == "patch":
                print(ForeColor.Yellow + "Une mise à jour du dernier patch de League of Legends est disponible",
                      "dans le Data Dragon." + FontStyle.Normal)

            input("Appuyez sur Entrer pour commencer la mise à jour...")
            update_ddragon(latest_version, installed_version, ddragon_path)
    else:
        # Le Data Dragon n'a pas encore été installé. On va donc procéder à son installation.
        print(ForeColor.Yellow + "Le Data Dragon n'est pas encore installé." + FontStyle.Normal)

        if input("Voulez-vous effectuer une installation complète du Data Dragon (Oui / Non) ? ") == "Oui":
            fresh_ddragon_install_all(ddragon_path)
        else:
            fresh_ddragon_install_latest(ddragon_path, latest_version)
else:
    clear_console()
    print(ForeColor.Red + "Certaines informations requises sont manquantes. Impossible de continuer l'exécution.",
          FontStyle.Normal)
