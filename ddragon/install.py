from lolddragon.system.console import clear_console
from lolddragon.assets.colors.fore import ForeColor
from lolddragon.assets.font import FontStyle
from lolddragon.ddragon.common import *
from lolddragon.riotapi.lol.ddragonext import get_ddragon_file_extension
from lolddragon.riotapi.lol.versions import get_game_versions_list
import os
from subprocess import call


# Installe uniquement la dernière version disponible du Data Dragon.
# Le Data Dragon sera plus rapide à télécharger et à installer, mais contiendra moins de fichiers.
def fresh_ddragon_install_latest(ddragon_folder, version):
    temp_folder = os.path.join(ddragon_folder, "temp")
    file_name = "LoL_DDragon_" + version + "." + get_ddragon_file_extension(version)

    # Création du répertoire temporaire avant de commencer
    if os.path.exists(temp_folder) is False:
        os.mkdir(temp_folder)

    create_git_repo(ddragon_folder)
    clear_console()
    download_version(temp_folder, file_name, version)
    extract_version(temp_folder, file_name, version)
    remove_downloaded_file(temp_folder, file_name)
    update_ddragon_folders_name(temp_folder, version)
    move_ddragon_version(temp_folder, ddragon_folder, version)
    clear_console()
    add_version_to_git(ddragon_folder, version)

    # Suppression du répertoire temporaire
    if os.path.exists(temp_folder):
        os.removedirs(temp_folder)

    clear_console()
    print(ForeColor.Green + "Le Data Dragon a été installé avec succès." + FontStyle.Normal)


# Installe l'intégralité du Data Dragon.
# Le Data Dragon sera plus long à télécharger et à installer, mais contiendra tous les fichiers existants sur le jeu.
def fresh_ddragon_install_all(ddragon_folder):
    versions_list = get_game_versions_list()
    temp_folder = os.path.join(ddragon_folder, "temp")

    # Création du répertoire temporaire avant de commencer
    if os.path.exists(temp_folder) is False:
        os.mkdir(temp_folder)

    clear_console()
    create_git_repo(ddragon_folder)

    # Installation de chaque version disponible
    for version in versions_list:
        file_name = "LoL_DDragon_" + version + "." + get_ddragon_file_extension(version)
        clear_console()
        download_version(temp_folder, file_name, version)
        extract_version(temp_folder, file_name, version)
        remove_downloaded_file(temp_folder, file_name)
        update_ddragon_folders_name(temp_folder, version)
        move_ddragon_version(temp_folder, ddragon_folder, version)
        clear_console()
        add_version_to_git(ddragon_folder, version)

    # Suppression du répertoire temporaire
    if os.path.exists(temp_folder):
        os.removedirs(temp_folder)

    clear_console()
    print(ForeColor.Green + "Le Data Dragon a été installé avec succès." + FontStyle.Normal)


# Créer le dépôt Git en local, et le fichier .gitignore
def create_git_repo(ddragon_folder):
    print("Création du dépôt Git...")
    call("git init", cwd=ddragon_folder, shell=True)

    print("Création du fichier d'exclusion...")
    gitignore = open(os.path.join(ddragon_folder, ".gitignore"), "a")
    gitignore.write("temp/")
    gitignore.close()

    print("Ajout du fichier d'exclusion au dépôt Git...")
    call("git add .", cwd=ddragon_folder, shell=True)
    call("git commit -m \"Added .gitignore\"", cwd=ddragon_folder, shell=True)

    print("Dépôt Git créé.")
