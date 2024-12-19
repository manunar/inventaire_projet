import os
import unittest
from export_report import export_report


class TestExportReport(unittest.TestCase):
    def setUp(self):
        self.output_file = "data/test_export.csv"
        self.data = [
            {"Nom du produit": "Produit A", "Catégorie": "Électronique", "Quantité": "10", "Prix unitaire (€)": "99.99",
             "Description": "Test A"},
            {"Nom du produit": "Produit B", "Catégorie": "Vêtements", "Quantité": "20", "Prix unitaire (€)": "49.99",
             "Description": "Test B"},
        ]

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_export_report_creates_file(self):
        export_report(self.data, self.output_file)
        self.assertTrue(os.path.exists(self.output_file), "Le fichier d'export n'a pas été créé.")

    def test_export_report_correct_data(self):
        export_report(self.data, self.output_file)
        with open(self.output_file, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(len(lines) - 1, len(self.data), "Le nombre d'enregistrements exportés est incorrect.")


if __name__ == "__main__":
    unittest.main()
