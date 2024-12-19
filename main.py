import os
import argparse
from generate_data import generate_fake_inventory
from search_inventory import load_inventory, search_inventory
from export_report import export_report

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "inventaire_fictif.csv")


def main():
    # Configuration d'argparse
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire.")

    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    # Commande pour générer des données
    generate_parser = subparsers.add_parser("generate", help="Générer des données fictives")
    generate_parser.add_argument("-n", "--num-records", type=int, required=True, help="Nombre de lignes à générer")

    # Commande pour rechercher des données
    search_parser = subparsers.add_parser("search", help="Rechercher un produit")
    search_parser.add_argument("-f", "--field", type=str, required=True,
                               help="Champ à rechercher (Nom du produit, Catégorie, etc.)")
    search_parser.add_argument("-v", "--value", type=str, required=True, help="Valeur à rechercher")

    # Commande pour exporter un rapport
    export_parser = subparsers.add_parser("export", help="Exporter un rapport")
    export_parser.add_argument("-o", "--output", type=str, required=True,
                               help="Nom du fichier d'export (ex: rapport.csv)")

    # Analyse des arguments
    args = parser.parse_args()

    # Assurez-vous que le dossier data existe
    os.makedirs(DATA_DIR, exist_ok=True)

    if args.command == "generate":
        generate_fake_inventory(FILE_PATH, args.num_records)

    elif args.command == "search":
        if not os.path.exists(FILE_PATH):
            print("Aucun inventaire trouvé. Veuillez d'abord générer des données.")
            return

        inventory = load_inventory(FILE_PATH)
        results = search_inventory(inventory, args.field, args.value)
        if results:
            print("\nRésultats trouvés :")
            for item in results:
                print(item)
        else:
            print("Aucun produit trouvé.")

    elif args.command == "export":
        if not os.path.exists(FILE_PATH):
            print("Aucun inventaire trouvé. Veuillez d'abord générer des données.")
            return

        inventory = load_inventory(FILE_PATH)
        export_report(inventory, os.path.join(DATA_DIR, args.output))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
