# Système de Gestion d'Inventaire Fictif

Bienvenue dans le **Système de Gestion d'Inventaire Fictif** ! Ce projet vous permet de générer, rechercher et exporter un inventaire fictif à l'aide de commandes simples en ligne de commande.

## Utilisation

Ce projet permet de générer, rechercher et exporter un inventaire fictif à l'aide de commandes en ligne de commande. Voici comment l'utiliser.

---

## Commandes Disponibles

### 1. Générer des Données Fictives

Cette commande permet de générer un inventaire fictif avec des produits aléatoires. Vous devez spécifier le nombre de produits à générer.

```bash
python main.py generate -n <nombre_de_lignes>
```
### 2.  Rechercher des Produits

Cette commande permet de rechercher un produit dans l'inventaire en fonction d'un champ spécifique (par exemple, "Nom du produit" ou "Catégorie").

```bash
python main.py search -f <champ> -v <valeur>
```
### 3. Exporter l'Inventaire Sous Forme de Rapport

Cette commande vous permet d'exporter l'inventaire sous forme de fichier CSV. Vous devez spécifier le nom du fichier d'export.

```bash

python main.py export -o <nom_du_fichier>
```

