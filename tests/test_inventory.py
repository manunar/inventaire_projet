import unittest
import os
import csv
import tempfile
import shutil  # Ajout de shutil pour la suppression récursive
from generate_data import generate_fake_inventory
from search_inventory import load_inventory, search_inventory
from export_report import export_report


class TestInventoryManagement(unittest.TestCase):
    def setUp(self):
        """Préparation des tests avec un fichier temporaire"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_inventory.csv")
        self.test_data = [
            {
                'Nom du produit': 'Test Product',
                'Catégorie': 'Électronique',
                'Quantité': '10',
                'Prix unitaire (€)': '99.99',
                'Description': 'Test description'
            },
            {
                'Nom du produit': 'Another Product',
                'Catégorie': 'Mobilier',
                'Quantité': '5',
                'Prix unitaire (€)': '199.99',
                'Description': 'Another description'
            }
        ]

    def tearDown(self):
        """Nettoyage après les tests en utilisant shutil"""
        try:
            shutil.rmtree(self.temp_dir)
        except Exception as e:
            print(f"Erreur lors du nettoyage: {e}")

    def create_test_file(self, data):
        """Helper pour créer un fichier de test avec des données spécifiques"""
        fieldnames = ['Nom du produit', 'Catégorie', 'Quantité', 'Prix unitaire (€)', 'Description']
        with open(self.test_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def test_generate_fake_inventory(self):
        """Test de la génération d'inventaire"""
        num_records = 10
        generate_fake_inventory(self.test_file, num_records)

        self.assertTrue(os.path.exists(self.test_file))
        inventory = load_inventory(self.test_file)
        self.assertEqual(len(inventory), num_records)

        first_record = inventory[0]
        expected_fields = {'Nom du produit', 'Catégorie', 'Quantité', 'Prix unitaire (€)', 'Description'}
        self.assertEqual(set(first_record.keys()), expected_fields)

    def test_load_inventory(self):
        """Test du chargement de l'inventaire"""
        self.create_test_file(self.test_data)

        inventory = load_inventory(self.test_file)
        self.assertEqual(len(inventory), 2)
        self.assertEqual(inventory[0]['Nom du produit'], 'Test Product')
        self.assertEqual(inventory[1]['Catégorie'], 'Mobilier')

    def test_search_inventory(self):
        """Test de la recherche dans l'inventaire"""
        self.create_test_file(self.test_data)
        inventory = load_inventory(self.test_file)

        results = search_inventory(inventory, 'Catégorie', 'Électronique')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['Nom du produit'], 'Test Product')

        results = search_inventory(inventory, 'Catégorie', 'électronique')
        self.assertEqual(len(results), 1)

        results = search_inventory(inventory, 'Catégorie', 'Inexistant')
        self.assertEqual(len(results), 0)

    def test_export_report(self):
        """Test de l'export du rapport"""
        output_file = os.path.join(self.temp_dir, "export_test.csv")
        export_report(self.test_data, output_file)

        self.assertTrue(os.path.exists(output_file))

        exported_inventory = load_inventory(output_file)
        self.assertEqual(len(exported_inventory), 2)
        self.assertEqual(exported_inventory[0], self.test_data[0])

    def test_empty_export(self):
        """Test de l'export avec des données vides"""
        output_file = os.path.join(self.temp_dir, "empty_export.csv")
        export_report([], output_file)
        self.assertFalse(os.path.exists(output_file))


if __name__ == '__main__':
    unittest.main(verbosity=2)