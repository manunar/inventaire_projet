import csv

def export_report(results, output_file):
    """
    Exporte un rapport à partir d’une liste de résultats dans un fichier CSV.

    PRE :
        - results (list) : liste de dictionnaires contenant les résultats.
        - output_file (str) : chemin du fichier CSV à créer.

    POST :
        - Un fichier CSV est créé avec les résultats.

    RAISE :
        - IOError : si une erreur survient lors de l’écriture du fichier.
    """
    try:
        if not results:
            print("Aucun résultat à exporter.")
            return
        keys = results[0].keys()
        with open(output_file, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)
        print(f"Rapport exporté dans {output_file}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")
        raise
