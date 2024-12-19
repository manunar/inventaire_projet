import csv
import random
from faker import Faker

def generate_fake_inventory(output_file, num_records):
    fake = Faker()
    categories = ['Électronique', 'Alimentation', 'Vêtements', 'Mobilier', 'Jouets']

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
