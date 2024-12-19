import csv

def load_inventory(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        inventory = [row for row in reader]
    return inventory

def search_inventory(inventory, field, value):
    return [item for item in inventory if str(item[field]).lower() == str(value).lower()]
