from Voiture import Voiture


class Board:
    """
    taille 10x10
    liste_voitures
    effectuer_un_tour() # bouge tous les pompiers ou le fait attendre sur un feu
    afficher() # affiche la position des pompiers et des feux
    """

    def __init__(self):
        self.liste_voitures = [Voiture([2, 1]), Voiture([3, 4])]

    def est_voiture(self, i, j):
        for voit in self.liste_voitures:
            if i == voit.get_position()[0] and j == voit.get_position()[1]:
                return True
        return False

    def get_char(self, i, j):
        if self.est_voiture(i, j):
            return 'X'
#         if (i,j) in self.liste_feux:
#             return 'O'
        return ' '

    def afficher(self):
        for j in range(10):
            print([self.get_char(i, j) for i in range(10)])

    def effectuer_un_tour(self):
        for voit in self.liste_voitures:
            voit.avancer()
            if voit.est_au_bord():
                voit.reculer()
                voit.tourner2()
