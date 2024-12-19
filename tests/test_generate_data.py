import os
import unittest
from generate_data import generate_fake_inventory


class TestGenerateData(unittest.TestCase):
    def setUp(self):
        self.output_file = "data/test_inventory.csv"
        self.num_records = 10

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_fake_inventory_creates_file(self):
        generate_fake_inventory(self.output_file, self.num_records)
        self.assertTrue(os.path.exists(self.output_file), "Le fichier n'a pas été créé.")

    def test_generate_fake_inventory_correct_record_count(self):
        generate_fake_inventory(self.output_file, self.num_records)
        with open(self.output_file, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(len(lines) - 1, self.num_records, "Le nombre d'enregistrements générés est incorrect.")


if __name__ == "__main__":
    unittest.main()
