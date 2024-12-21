import numpy as np

from .theoretic.constant_sum_games import ConstantSumGame

class MatchingPenniesGame(ConstantSumGame):
    def __init__(self, a:int=1, b:int=0):
        """
        compare pennies.
        When two players, compare pennies.
        When both players show heads playerA gets the pennies.
        When both players show tail, playerB get the Pennies.

        Max. Competitive Game

        Parameters
        ----------
        a
        b
        """

        super().__init__(n_players=2)
        self.metric = np.array([[(a, b), (b, b)], [(b, b), (b, a)]])

    def draw(self, playerA: bool, playerB: bool) -> tuple[float, float]:
        return self.metric[playerA, playerB]
