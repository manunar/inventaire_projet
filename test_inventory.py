import unittest
import os
import csv
import tempfile
import shutil
from generate_data import generate_fake_inventory
from search_inventory import load_inventory, search_inventory
from export_report import export_report

class TestInventoryManagement(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_inventory.csv")
        self.test_data = [
            {'Nom du produit': 'Produit Test', 'Catégorie': 'Électronique', 'Quantité': '10', 'Prix unitaire (€)': '99.99', 'Description': 'Test description'},
            {'Nom du produit': 'Autre Produit', 'Catégorie': 'Mobilier', 'Quantité': '5', 'Prix unitaire (€)': '199.99', 'Description': 'Another description'}
        ]

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def create_test_file(self, data):
        fieldnames = ['Nom du produit', 'Catégorie', 'Quantité', 'Prix unitaire (€)', 'Description']
        with open(self.test_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def test_generate_fake_inventory(self):
        num_records = 10
        generate_fake_inventory(self.test_file, num_records)
        self.assertTrue(os.path.exists(self.test_file))
        inventory = load_inventory(self.test_file)
        self.assertEqual(len(inventory), num_records)

    def test_load_inventory(self):
        self.create_test_file(self.test_data)
        inventory = load_inventory(self.test_file)
        self.assertEqual(len(inventory), 2)

    def test_search_inventory(self):
        self.create_test_file(self.test_data)
        inventory = load_inventory(self.test_file)
        results = search_inventory(inventory, 'Catégorie', 'Électronique')
        self.assertEqual(len(results), 1)

    def test_export_report(self):
        output_file = os.path.join(self.temp_dir, "export_test.csv")
        export_report(self.test_data, output_file)
        self.assertTrue(os.path.exists(output_file))
