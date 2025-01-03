import os
import csv
import random
import argparse
from faker import Faker
from export_report import export_report
from search_inventory import load_inventory, search_inventory

data_dir = os.path.join(os.getcwd(), "data")
os.makedirs(data_dir, exist_ok=True)

def generate_fake_inventory(output_file, num_records):
    """
    Génère un fichier CSV contenant un inventaire fictif.

    PRE :
        - output_file (str) : chemin d’accès au fichier CSV à générer.
        - num_records (int) : nombre de lignes à générer (doit être > 0).

    POST :
        - Un fichier CSV contenant num_records lignes est créé.

    RAISE :
        - ValueError : si num_records <= 0.
        - IOError : si une erreur survient lors de l'écriture du fichier.
    """
    if num_records <= 0:
        raise ValueError("Le nombre d'enregistrements doit être supérieur à 0.")

    fake = Faker()
    categories = ['Électronique', 'Alimentation', 'Vêtements', 'Mobilier', 'Jouets']

    try:
        with open(output_file, mode="w", encoding="utf-8", newline="") as f:
            fieldnames = ['Nom du produit', 'Catégorie', 'Quantité', 'Prix unitaire (€)', 'Description']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(num_records):
                product_name = fake.word().capitalize() + " " + fake.word().capitalize()
                category = random.choice(categories)
                quantity = random.randint(1, 500)
                price = round(random.uniform(5.0, 500.0), 2)
                description = fake.sentence(nb_words=6)

                writer.writerow({
                    'Nom du produit': product_name,
                    'Catégorie': category,
                    'Quantité': quantity,
                    'Prix unitaire (€)': price,
                    'Description': description
                })
        print(f"Fichier CSV généré : {output_file}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")
        raise

def merge_files(file_paths, output_file):
    """
    Fusionne plusieurs fichiers CSV d'inventaire en un seul.

    PRE :
        - file_paths (list) : liste des chemins de fichiers à fusionner.
        - output_file (str) : chemin du fichier de sortie.

    POST :
        - Un fichier CSV contenant les données fusionnées est créé.

    RAISE :
        - IOError : si une erreur survient lors de la lecture ou de l'écriture d'un fichier.
    """
    combined_data = []
    for file_path in file_paths:
        full_path = os.path.join(data_dir, file_path) if not os.path.dirname(file_path) else file_path
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
        try:
            export_report(combined_data, os.path.join(data_dir, output_file))
            print(f"\nFusion terminée. Fichier créé : {output_file}")
            print(f"Nombre total d'enregistrements : {len(combined_data)}")
        except IOError as e:
            print(f"Erreur lors de l'exportation du fichier fusionné : {e}")
            raise
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

    if args.command == "generate":
        for i in range(args.multiple):
            file_name = f"inventaire_fictif_{i + 1}.csv"
            file_path = os.path.join(data_dir, file_name)
            generate_fake_inventory(file_path, args.num_records)

    elif args.command == "search":
        default_inventory = os.path.join(data_dir, "inventaire_fictif_1.csv")
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
                export_path = os.path.join(data_dir, args.export)
                export_report(results, export_path)
                print(f"\nRésultats exportés dans : {export_path}")
        else:
            print("Aucun produit trouvé.")

    elif args.command == "merge":
        merge_files(args.files, args.output)

    else:
        parser.print_help()


def interactive_shell():
    """
    Interface interactive pour gérer l'inventaire via un shell.
    """
    while True:
        print("\n=== Système de gestion d'inventaire ===")
        print("1. Générer des données fictives")
        print("2. Rechercher un produit")
        print("3. Fusionner des fichiers")
        print("4. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            try:
                num_records = int(input("Nombre de lignes à générer : "))
                multiple_files = int(input("Nombre de fichiers à générer : "))
                for i in range(multiple_files):
                    file_name = f"inventaire_fictif_{i + 1}.csv"
                    file_path = os.path.join(data_dir, file_name)
                    generate_fake_inventory(file_path, num_records)
            except ValueError:
                print("Veuillez entrer un nombre valide.")
            except Exception as e:
                print(f"Erreur : {e}")

        elif choice == "2":
            field = input("Champ à rechercher : ")
            value = input("Valeur à rechercher : ")
            default_inventory = os.path.join(data_dir, "inventaire_fictif_1.csv")
            if os.path.exists(default_inventory):
                inventory = load_inventory(default_inventory)
                results = search_inventory(inventory, field, value)
                if results:
                    print("\nRésultats trouvés :")
                    for item in results:
                        print(item)
                    export = input("Voulez-vous exporter les résultats ? (y/n) : ")
                    if export.lower() == "y":
                        export_path = input("Nom du fichier d'export (ex: resultats.csv) : ")
                        export_report(results, os.path.join(data_dir, export_path))
                else:
                    print("Aucun produit trouvé.")
            else:
                print("Aucun inventaire trouvé. Veuillez d'abord générer des données.")

        elif choice == "3":
            files = input("Liste des fichiers à fusionner (séparés par des espaces) : ").split()
            output_file = input("Nom du fichier d'export : ")
            merge_files(files, output_file)

        elif choice == "4":
            print("Merci d'avoir utilisé le système.")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


def main():
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire.")
    parser.add_argument("--interactive", action="store_true", help="Lancer l'interface interactive")
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

    if args.interactive:
        interactive_shell()
    elif args.command == "generate":
        for i in range(args.multiple):
            file_name = f"inventaire_fictif_{i + 1}.csv"
            file_path = os.path.join(data_dir, file_name)
            generate_fake_inventory(file_path, args.num_records)
    elif args.command == "search":
        default_inventory = os.path.join(data_dir, "inventaire_fictif_1.csv")
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
                export_path = os.path.join(data_dir, args.export)
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
