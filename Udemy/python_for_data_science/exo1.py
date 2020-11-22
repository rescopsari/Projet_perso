# Exercice sur les listes

# Objectif : Manipuler une liste contenant les notes de 20 élèves 

# 1. Créer une liste nommée « mes_notes » qui contient les nombres suivant : 19,7,15,9,10,6,18,10,16,14,13,10,2,20,17,8,12,10,11,4
# 2. Calculer la moyenne générale de cette classe de 20 élèves et ranger le résultat dans une variable nommée « moyenne_generale »
# 3. Trouver la note la plus faible et la note la plus élevée
# 4. Trier la liste des notes de la plus grande à la plus petite
# 5. Remplacer la note 2 par 6
# 6. Compter le nombre de notes égales à 10 dans la classe
# 7. Trouver le nombre d’élèves avec une note > 10 


import numpy as np

mes_notes = [19,7,15,9,10,6,18,10,16,14,13,10,2,20,17,8,12,10,11,4]

moyene_general = np.mean(mes_notes)
note_min = min(mes_notes)
note_max = max(mes_notes)

print(f"La note la plus basse est : {note_min}")
print(f"La note la plus grande est : {note_max}")

mes_notes.sort(reverse=True)

mes_notes[19] = 6

mes_notes.count(10)

mes_notes_array = np.asarray(mes_notes)
len(mes_notes_array[mes_notes_array > 10])

