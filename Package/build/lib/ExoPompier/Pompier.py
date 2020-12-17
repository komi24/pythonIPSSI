
class Pompier:
    """
    position
    est_occupe
    """

    def __init__(self, board, position_init):
        self.position = position_init
        self.board = board
        self.est_occupe = 0

    def se_deplacer_vers(self, position_feu):
        if self.est_occupe == 0:
            if self.position[0] < position_feu[0]:
                self.position[0] += 1
            elif self.position[0] > position_feu[0]:
                self.position[0] -= 1
            elif self.position[1] < position_feu[1]:
                self.position[1] += 1
            elif self.position[1] > position_feu[1]:
                self.position[1] -= 1
            else:
                self.board.eteindre(position_feu)
                self.est_occupe = 5
        else:
            self.est_occupe -= 1
