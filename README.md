Utilisation
Ce projet permet de générer, rechercher et exporter un inventaire fictif à l'aide de commandes en ligne de commande. Voici comment l'utiliser.

Prérequis
Avant d'utiliser les commandes, assurez-vous que les bibliothèques nécessaires sont installées :

bash
Copier le code
pip install faker
Commandes disponibles
Générer des données fictives

Cette commande permet de générer un inventaire fictif avec des produits aléatoires. Vous devez spécifier le nombre de produits à générer.

Syntaxe
bash
Copier le code
python main.py generate -n <nombre_de_lignes>
Exemple
Pour générer 100 produits :

bash
Copier le code
python main.py generate -n 100
Cela créera un fichier data/inventaire_fictif.csv contenant 100 produits fictifs.

Rechercher des produits

Cette commande permet de rechercher un produit dans l'inventaire en fonction d'un champ spécifique (par exemple, "Nom du produit" ou "Catégorie").

Syntaxe
bash
Copier le code
python main.py search -f <champ> -v <valeur>
Exemple
Pour rechercher des produits de la catégorie "Électronique" :

bash
Copier le code
python main.py search -f "Catégorie" -v "Électronique"
Cette commande affichera les produits qui appartiennent à la catégorie "Électronique".

Exporter l'inventaire sous forme de rapport

Cette commande permet d'exporter l'inventaire actuel dans un fichier CSV. Vous devez spécifier le nom du fichier d'export.

Syntaxe
bash
Copier le code
python main.py export -o <nom_du_fichier>
Exemple
Pour exporter l'inventaire dans un fichier appelé rapport.csv :

bash
Copier le code
python main.py export -o rapport.csv
Cette commande générera un fichier rapport.csv contenant l'inventaire complet.
