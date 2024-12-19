import os
import argparse
from generate_data import generate_fake_inventory
from search_inventory import load_inventory, search_inventory
from export_report import export_report

DATA_DIR = os.path.join(os.getcwd(), "data")


def merge_files(file_paths, output_file):
    combined_data = []
    for file_path in file_paths:
        # Construire le chemin complet si nécessaire
        full_path = os.path.join(DATA_DIR, file_path) if not os.path.dirname(file_path) else file_path
        if os.path.exists(full_path):
            try:
                inventory = load_inventory(full_path)
                combined_data.extend(inventory)
                print(f"Fichier fusionné avec succès : {file_path}")
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
        else:
            print(f"Fichier non trouvé : {file_path}")

    if combined_data:
        output_path = os.path.join(DATA_DIR, output_file)
        export_report(combined_data, output_path)
        print(f"\nFusion terminée. Fichier créé : {output_path}")
        print(f"Nombre total d'enregistrements : {len(combined_data)}")
    else:
        print("Aucune donnée à fusionner.")


def main():
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire.")
    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    # Commande pour générer des données
    generate_parser = subparsers.add_parser("generate", help="Générer des données fictives")
    generate_parser.add_argument("-n", "--num-records", type=int, required=True, help="Nombre de lignes à générer")
    generate_parser.add_argument("-m", "--multiple", type=int, default=1, help="Nombre de fichiers à générer")

    # Commande pour rechercher des données
    search_parser = subparsers.add_parser("search", help="Rechercher un produit")
    search_parser.add_argument("-f", "--field", type=str, required=True, help="Champ à rechercher")
    search_parser.add_argument("-v", "--value", type=str, required=True, help="Valeur à rechercher")
    search_parser.add_argument("-e", "--export", type=str, help="Exporter les résultats dans un fichier CSV")

    # Commande pour fusionner des fichiers
    merge_parser = subparsers.add_parser("merge", help="Fusionner plusieurs fichiers")
    merge_parser.add_argument("-f", "--files", type=str, nargs="+", required=True, help="Liste de fichiers à fusionner")
    merge_parser.add_argument("-o", "--output", type=str, required=True, help="Nom du fichier d'export")

    args = parser.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)

    if args.command == "generate":
        for i in range(args.multiple):
            file_name = f"inventaire_fictif_{i + 1}.csv"
            file_path = os.path.join(DATA_DIR, file_name)
            generate_fake_inventory(file_path, args.num_records)

    elif args.command == "search":
        default_inventory = os.path.join(DATA_DIR, "inventaire_fictif_1.csv")
        if not os.path.exists(default_inventory):
            print("Aucun inventaire trouvé. Veuillez d'abord générer des données.")
            return

        inventory = load_inventory(default_inventory)
        results = search_inventory(inventory, args.field, args.value)
        if results:
            print("\nRésultats trouvés :")
            for item in results:
                print(item)

            if args.export:
                export_path = os.path.join(DATA_DIR, args.export)
                export_report(results, export_path)
                print(f"\nRésultats exportés dans : {export_path}")
        else:
            print("Aucun produit trouvé.")

    elif args.command == "merge":
        merge_files(args.files, args.output)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()