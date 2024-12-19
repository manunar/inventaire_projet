import csv

def load_inventory(file_path):
    inventory = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            inventory.append(row)
    return inventory

def search_inventory(inventory, field, value):
    results = []
    for item in inventory:
        if value.lower() in item[field].lower():
            results.append(item)
    return results
