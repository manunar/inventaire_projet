import csv

def export_report(results, output_file):
    if not results:
        print("Aucun résultat à exporter.")
        return
    keys = results[0].keys()
    with open(output_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
    print(f"Rapport exporté dans {output_file}")
