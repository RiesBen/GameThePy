import numpy as np


class PrisonersDilemmaGame():

    def __init__(self, a=1, b1=2,b2=-1,c=-2):
        self.metric = np.array([[(a,a),(b1, b2)],[(b2, b1),(c,c)]]

    def draw(self, playerA:bool, playerB:bool)->tuple[float, float]:
        return self.metric[playerA, playerB]

