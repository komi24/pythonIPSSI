from Pompier import Pompier
from random import randint


class Board:
    """
    taille 10x10
    liste_pompiers
    liste_feux
    effectuer_un_tour() # bouge tous les pompiers ou le fait attendre sur un feu
    afficher() # affiche la position des pompiers et des feux
    """

    def __init__(self):
        self.liste_pompiers = [Pompier(self, [5, 3]), Pompier(
            self, [5, 7]), Pompier(self, [2, 3])]
        self.liste_feux = [(randint(0, 9), randint(0, 9)) for i in range(10)]

    def distance(self, position1, position2):
        return abs(position2[0] - position1[0]) + abs(position2[1] - position1[1])

    def eteindre(self, position):
        self.liste_feux.remove(position)

    def feu_le_plus_proche(self, position):
        min_dist = self.distance(self.liste_feux[0],  position)
        feu_proche = self.liste_feux[0]
        for feu in self.liste_feux[1:]:
            if self.distance(feu,  position) < min_dist:
                feu_proche = feu
                min_dist = self.distance(feu,  position)
        return feu_proche

    def est_pompier(self, i, j):
        for pomp in self.liste_pompiers:
            if pomp.position[0] == i and pomp.position[1] == j:
                return True
        return False

    def get_char(self, i, j):
        if self.est_pompier(i, j):
            return 'X'
        if (i, j) in self.liste_feux:
            return 'O'
        return ' '

    def afficher(self):
        for j in range(10):
            print([self.get_char(i, j) for i in range(10)])

    def effectuer_un_tour(self):
        for pomp in self.liste_pompiers:
            pomp.se_deplacer_vers(self.feu_le_plus_proche(pomp.position))
