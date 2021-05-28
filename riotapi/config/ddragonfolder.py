import os
from assets.colors.fore import ForeColor
from assets.font import FontStyle


# Retourne le chemin d'accès vers le dossier du Data Dragon, depuis le fichier de configuration dédié
def get_ddragon_folder():
    file_path = os.path.join(os.path.abspath(os.getcwd()), "config/ddragonfolder.txt")

    if (os.path.exists(file_path)):
        ddragonfolder_file = open(file_path, "r")
        ddragonfolder_file_lines = ddragonfolder_file.readlines()

        if len(ddragonfolder_file_lines) > 0:
            ddragonfolder = ddragonfolder_file_lines[0]

            if os.path.exists(ddragonfolder):
                return ddragonfolder
            else:
                print(ForeColor.Yellow + "Chemin d'accès au dossier du Data Dragon est incorrect." + FontStyle.Normal)
        else:
            print(ForeColor.Red + "Aucun chemin d'accès au dossier du Data Dragon renseigné." + FontStyle.Normal)
    else:
        print(ForeColor.Red + "Fichier de configuration du chemin d'accès au dossier du Data Dragon introuvable.",
              FontStyle.Normal)

    return False
