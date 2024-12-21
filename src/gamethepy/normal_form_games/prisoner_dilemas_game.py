
import numpy as np

from .theoretic.normal_form_games import NormalFormGame

class PrisonersDilemmaGame(NormalFormGame):

    def __init__(self, a=-1, b=0, c=-4, d=-3):
        """

        TCP internet Protocol or PrisonersDilemma
        Rule: c > a > d > b

        A Mixture between Competitive&Cooperative

        Parameters
        ----------
        a
        b
        c
        c
        """
        self.metric = np.array([[(a,a), (b, c)], [(c, b), (d, d)]])

    def draw(self, playerA:bool, playerB:bool)->tuple[float, float]:
        return self.metric[playerA, playerB]
