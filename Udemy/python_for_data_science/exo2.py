# Exercice : manipuler les prix de 58 maisons
# Objectif : Manipuler une liste contenant les prix de 58 maisons

# Ensemble : Créer une liste nommée « prix_de_58_maisons » contenant des prix entre 125000 et 700000 euros
# 1. Combien de maisons ont un prix supérieur ou égal à 300000 euros ?
# 2. Combien de maisons ont un prix compris entre 250000 et 400000 euros ?
# 3. Combien de maisons ont un prix qui n’est pas supérieur à 600000 euros ?
# 4. Combien de maisons ont un prix inférieur à 150000 euros ou supérieur à 650000 euros ?

# Aide : parcourir la liste avec une boucle, utiliser des instructions de condition if et un compteur pour compter les résultats vrais.

import numpy as np

prix_de_58_maisons = list(range(125000, 700000, 10000))

# 1 
nombre_maisons = 0
for prix in prix_de_58_maisons:
    if (prix >= 300000):
        nombre_maisons += 1
print(f"Le nombre de maisons avec un prix supérieur ou égal à 300000 euros est de {nombre_maisons}")

# 2 
nombre_maisons = 0
for prix in prix_de_58_maisons:
    if (prix >= 300000) and (prix <= 400000):
        nombre_maisons += 1
print(f"Le nombre de maisons avec un prix compris entre 250000 et 400000 euros est de {nombre_maisons}")

# 3
nombre_maisons = 0
for prix in prix_de_58_maisons:
    if not (prix > 600000):
        nombre_maisons += 1
print(f"Le nombre de maisons avec un prix qui n’est pas supérieur à 600000 euros est de {nombre_maisons}")

# 4
nombre_maisons = 0
for prix in prix_de_58_maisons:
    if (prix < 150000) or (prix > 650000):
        nombre_maisons += 1
print(f"Le nombre de maisons avec un prix inférieur à 150000 euros ou supérieur à 650000 euros est de {nombre_maisons}")

