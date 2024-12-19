# t201 Script perso

Un script Python pour gérer un inventaire :
- Génération de données fictives avec `Faker`.
- Recherche rapide d'informations (par produit, catégorie, etc.).
- Export de rapports au format CSV.

## Fonctionnalités

1. **Génération des données** :
   ```bash
   python main.py generate --output data/inventory.csv --count 100
