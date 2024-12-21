import numpy as np

from .theoretic.constant_sum_games import ConstantSumGame

class RockPaperScissorsGame(ConstantSumGame):
    def __init__(self, a:int=1, b:int=0, c:int=-1):
        """
        Competitive Game

        Parameters
        ----------
        a
        b
        """

        super().__init__(n_players=2)
        self.metric = np.array([[(b, b), (a, c), (c,a)], [(c,a), (b, b), (a, c)], [(a,c), (c, a), (b, b)]])

    def draw(self, playerA:int, playerB:int) -> tuple[float, float]:
        return self.metric[playerA, playerB]
