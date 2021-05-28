from assets.colors.fore import ForeColor
from assets.font import FontStyle
from ddragon.common import *
from riotapi.lol.ddragonext import get_ddragon_file_extension
from riotapi.lol.versions import get_game_versions_list
from system.console import clear_console


# Met à jour le Data Dragon vers la dernière version disponible.
# Télécharge et installe toutes les versions sorties après celle installée.
def update_ddragon(latest_version, installed_version, ddragon_folder):
    versions_list = get_game_versions_list()
    temp_folder = os.path.join(ddragon_folder, "temp")

    # Création du répertoire temporaire avant de commencer
    if os.path.exists(temp_folder) is False:
        os.mkdir(temp_folder)

    for i in range(versions_list.index(installed_version) + 1, len(versions_list)):
        file_name = "LoL_DDragon_" + versions_list[i] + "." + get_ddragon_file_extension(versions_list[i])
        clear_console()
        download_version(temp_folder, file_name, versions_list[i])
        extract_version(temp_folder, file_name, versions_list[i])
        remove_downloaded_file(temp_folder, file_name)
        update_ddragon_folders_name(temp_folder, versions_list[i])
        move_ddragon_version(temp_folder, ddragon_folder, versions_list[i])
        clear_console()
        add_version_to_git(ddragon_folder, versions_list[i])

    # Suppression du répertoire temporaire
    if os.path.exists(temp_folder):
        os.removedirs(temp_folder)

    clear_console()
    print(ForeColor.Green + "Le Data Dragon a été mis à jour avec succès." + FontStyle.Normal)
