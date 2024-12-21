import numpy as np

from .theoretic.common_payoff_games import CommonPayoffGames

class DrivingLaneGame(CommonPayoffGames):
    def __init__(self, a:int=1, b:int=0):
        """
        Max. Coordinative game


        Parameters
        ----------
        a
        b
        """

        super().__init__(n_players=2)
        self.metric = np.array([[(a, a), (b, b)], [(b, b), (a, a)]])

    def draw(self, playerA: bool, playerB: bool) -> tuple[float, float]:
        return self.metric[playerA, playerB]
