import csv

def load_inventory(file_path):
    """
    Charge les données d’un fichier CSV d’inventaire.

    PRE :
        - file_path (str) : chemin du fichier CSV existant.

    POST :
        - Retourne une liste de dictionnaires représentant l’inventaire.

    RAISE :
        - FileNotFoundError : si le fichier est introuvable.
        - csv.Error : si une erreur survient lors de la lecture du fichier.
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
        return []
    except csv.Error as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
        return []

def search_inventory(inventory, field, value):
    """
    Recherche dans l’inventaire les enregistrements correspondant à une valeur donnée.

    PRE :
        - inventory (list) : liste de dictionnaires représentant l’inventaire.
        - field (str) : champ dans lequel rechercher.
        - value (str) : valeur à rechercher.

    POST :
        - Retourne une liste des enregistrements correspondants.

    RAISE :
        - KeyError : si le champ n’existe pas dans les enregistrements.
    """
    try:
        return [item for item in inventory if item[field].lower() == value.lower()]
    except KeyError as e:
        print(f"Erreur : champ '{field}' non trouvé dans l'inventaire.")
        return []
