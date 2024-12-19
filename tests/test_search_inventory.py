import unittest
from search_inventory import search_inventory

class TestSearchInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = [
            {"Nom du produit": "Produit A", "Catégorie": "Électronique", "Quantité": "10", "Prix unitaire (€)": "99.99", "Description": "Test A"},
            {"Nom du produit": "Produit B", "Catégorie": "Vêtements", "Quantité": "20", "Prix unitaire (€)": "49.99", "Description": "Test B"},
        ]

    def test_search_inventory_by_exact_name(self):
        result = search_inventory(self.inventory, "Nom du produit", "Produit A")
        self.assertEqual(len(result), 1, "Le produit recherché n'a pas été trouvé.")
        self.assertEqual(result[0]["Nom du produit"], "Produit A", "Mauvais produit trouvé.")

    def test_search_inventory_by_category(self):
        result = search_inventory(self.inventory, "Catégorie", "Électronique")
        self.assertEqual(len(result), 1, "Le produit dans la catégorie n'a pas été trouvé.")
        self.assertEqual(result[0]["Catégorie"], "Électronique", "Mauvaise catégorie trouvée.")

    def test_search_inventory_no_results(self):
        result = search_inventory(self.inventory, "Nom du produit", "Inexistant")
        self.assertEqual(len(result), 0, "Un produit inexistant a été trouvé.")

if __name__ == "__main__":
    unittest.main()
