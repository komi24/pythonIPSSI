import os
from time import sleep

from .Board import Board


"""
Pompiers peuvent se déplacer sur 4 directions (en haut, en bas, à gauche, à droite)
Bouge d'une case à chaque tour

Pour eteindre un feu, le pompier doit arriver SUR la case du feu et attendre 5 tours


1- Un pompier un feu 
2- Un pompier plusieurs feux (le pompier doit éteindre le feu et passer au feu suivant)
3- Plusieurs pompiers, plusieurs feux
"""

b = Board()

b.afficher()

while len(b.liste_feux) > 0:
    os.system("cls")
    b.effectuer_un_tour()
    b.afficher()
    sleep(0.2)
