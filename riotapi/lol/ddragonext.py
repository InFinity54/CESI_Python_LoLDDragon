# Détermine, en fonction de la version spécifiée, quelle est l'extension du fichier à télécharger
def get_ddragon_file_extension(version):
    if version.startswith("10.10"):
        return "zip"
    return "tgz"
