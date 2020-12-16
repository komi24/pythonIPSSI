import numpy as np


class Voiture:
    def __init__(self, position_param=[0, 0], vitesse_param=[1, 0]):
        self._position = np.array(position_param)
        self._vitesse = np.array(vitesse_param)

    def avancer(self):
        self._position += self._vitesse

    def reculer(self):
        self._position -= self._vitesse

    def accelerer(self):
        self._vitesse += 1

    def freiner(self):
        self._vitesse = 0

    def est_au_bord(self):
        return (self._position[0] < 0) or (self._position[0] > 9) or \
            self._position[1] < 0 or self._position[1] > 9

    def tourner2(self):
        self._vitesse = np.array([[0, -1], [1, 0]]).dot(self._vitesse)

    def tourner(self):
        if (self._vitesse == np.array([1, 0])).all():
            self._vitesse = np.array([0, 1])
        elif (self._vitesse == np.array([0, 1])).all():
            self._vitesse = np.array([-1, 0])
        elif (self._vitesse == np.array([-1, 0])).all():
            self._vitesse = np.array([0, -1])
        elif (self._vitesse == np.array([0, -1])).all():
            self._vitesse = np.array([1, 0])

    def get_position(self):
        return self._position
