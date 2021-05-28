from riotapi.lol.ddragonext import get_ddragon_file_extension
import requests
import os
import shutil
from subprocess import call
import tarfile
from tqdm import tqdm
import zipfile


# Génère le lien de téléchargement de la version du Data Dragon passée en paramètre.
def generate_download_link(version):
    return "https://ddragon.leagueoflegends.com/cdn/dragontail-" + version + "." + get_ddragon_file_extension(version)


# Fonction qui gère le téléchargement d'une version du Data Dragon
def download_version(ddragon_folder, file_name, version):
    # Code du téléchargement trouvé sur https://stackoverflow.com/a/15645088
    # Affichage de la progression inspiré du code utilisé pour l'extraction des fichiers tgz et zip
    with open(os.path.join(ddragon_folder, file_name), "wb") as f:
        print("Téléchargement de la version", version, "du Data Dragon...")
        response = requests.get(generate_download_link(version), stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            total_length = int(total_length)
            progress_bar = tqdm(total=total_length, unit="B", unit_scale=True)
            for data in response.iter_content(chunk_size=4096):
                f.write(data)
                progress_bar.update(len(data))
    print("")
    print("Téléchargement terminé.")


# Extraction d'une version du Data Dragon
def extract_version(ddragon_folder, file_name, version):
    print("Extraction de la version", version, "du Data Dragon...")

    # Code de l'extraction trouvé sur https://stackoverflow.com/a/53405055, puis remodifié légèrement
    if get_ddragon_file_extension(version) == "tgz":
        # Extraction d'un fichier .tgz
        ddragon_tgz = tarfile.open(name=os.path.join(ddragon_folder, file_name))
        for member in tqdm(iterable=ddragon_tgz.getmembers(), total=len(ddragon_tgz.getmembers()), unit=""):
            ddragon_tgz.extract(member=member, path=ddragon_folder)
        ddragon_tgz.close()
    else:
        # Extraction d'un fichier .zip
        ddragon_zip = zipfile.ZipFile(os.path.join(ddragon_folder, file_name), "r")
        for member in tqdm(iterable=ddragon_zip.infolist(), total=len(ddragon_zip.infolist()), unit=""):
            ddragon_zip.extract(member, ddragon_folder)
        ddragon_zip.close()

    print("Extraction terminée.")


# Suppression du fichier tgz/zip téléchargé
def remove_downloaded_file(folder_path, file_name):
    print("Suppression du fichier " + file_name + "...")
    os.remove(os.path.join(folder_path, file_name))
    print("Suppression terminée.")


# Mise en forme des dossiers du Data Dragon téléchargé
def update_ddragon_folders_name(ddragon_folder, version):
    print("Mise à jour des dossiers du Data Dragon...")
    version_split = version.split(".")
    simplified_version = version_split[0] + "." + version_split[1]

    if os.path.exists(os.path.join(ddragon_folder, version)):
        os.rename(os.path.join(ddragon_folder, version), os.path.join(ddragon_folder, "latest"))

    if os.path.exists(os.path.join(ddragon_folder, "lolpatch_" + version)):
        os.rename(os.path.join(ddragon_folder, version), os.path.join(ddragon_folder, "lolpatch_latest"))

    if os.path.exists(os.path.join(ddragon_folder, "lolpatch_" + simplified_version)):
        os.rename(os.path.join(ddragon_folder, "lolpatch_" + simplified_version),
                  os.path.join(ddragon_folder, "lolpatch_latest"))

    print("Dossiers mis à jour.")


# Ajoute la version du Data Dragon spécifiée au Git
def add_version_to_git(ddragon_folder, version):
    print("Ajout de la version", version, "au dépôt Git...")
    call("git add .", cwd=ddragon_folder, shell=True)
    call("git commit -m \"Added patch " + version + "\"", cwd=ddragon_folder, shell=True)
    print("Ajout au dépôt Git terminé.")


# Déplace les fichiers de la version courante dans le dossier racine du Data Dragon
def move_ddragon_version(temp_folder, ddragon_folder, version):
    print("Déplacement des fichiers de la version " + version + " vers le dossier du Data Dragon...")
    files_list = os.listdir(temp_folder)
    for file in tqdm(iterable=files_list, total=len(files_list), unit="Ko"):
        shutil.move(os.path.join(temp_folder, file), os.path.join(ddragon_folder, file))
    print("Déplacement des fichiers terminé.")
