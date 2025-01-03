import csv
import random
from faker import Faker

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
