# Système de Gestion d'Inventaire Fictif

Bienvenue dans le **Système de Gestion d'Inventaire Fictif** ! Ce projet vous permet de générer, rechercher, fusionner et exporter un inventaire fictif à l'aide de commandes simples en ligne de commande ou via une interface interactive.

## Utilisation

Ce projet permet de :
- Générer des fichiers d'inventaire fictifs avec des données aléatoires.
- Rechercher des produits dans un inventaire existant.
- Fusionner plusieurs fichiers d'inventaire.
- Exporter les résultats sous forme de rapport CSV.
- Utiliser une interface interactive pour une expérience utilisateur plus fluide.

---

## Commandes Disponibles

### 1. Interface Interactive

Cette commande lance un menu interactif permettant de naviguer entre les différentes fonctionnalités du projet sans avoir à utiliser plusieurs commandes.

```bash
python main.py --interactive
```

### 2. Générer des Données Fictives

Cette commande permet de générer un inventaire fictif avec des produits aléatoires. Vous devez spécifier le nombre de produits à générer et, optionnellement, le nombre de fichiers.

```bash
python main.py generate -n <nombre_de_lignes> -m <nombre_de_fichiers>
```

Exemple :
```bash
python main.py generate -n 100 -m 2
```
Cela génère 2 fichiers contenant chacun 100 lignes de données.

### 3. Rechercher des Produits

Cette commande permet de rechercher un produit dans l'inventaire en fonction d'un champ spécifique (par exemple, "Nom du produit" ou "Catégorie"). Vous pouvez également exporter les résultats.

```bash
python main.py search -f <champ> -v <valeur> [-e <nom_du_fichier_export>]
```

Exemple :
```bash
python main.py search -f "Catégorie" -v "Électronique" -e "resultats.csv"
```

### 4. Fusionner des Fichiers d'Inventaire

Cette commande permet de fusionner plusieurs fichiers CSV d'inventaire en un seul fichier.

```bash
python main.py merge -f <fichiers_à_fusionner> -o <nom_du_fichier_output>
```

Exemple :
```bash
python main.py merge -f inventaire_fictif_1.csv inventaire_fictif_2.csv -o inventaire_complet.csv
```

### 5. Exporter l'Inventaire Sous Forme de Rapport

Cette commande vous permet d'exporter l'inventaire ou les résultats d'une recherche sous forme de fichier CSV.

```bash
python main.py export -o <nom_du_fichier>
```

---

## Tests Unitaires

Des tests unitaires sont disponibles pour vérifier le bon fonctionnement des différentes fonctionnalités. Pour exécuter les tests :

```bash
python -m unittest discover tests
```

---

## Dépendances

Assurez-vous d'installer les dépendances avant d'exécuter le projet :

```bash
pip install -r requirements.txt
```
py export -o <nom_du_fichier>
```

