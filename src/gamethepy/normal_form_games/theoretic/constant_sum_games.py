import sympy as sp

from .normal_form_games import NormalFormGame

class ConstantSumGame(NormalFormGame):

    def __init__(self, n_players:int, constant_sum:float=0):
        """
        Or Zero Sum Game
        Mainly two player games

        Pure Competition situation. Extrem Situation.

        #Todo: Realize  u_1(a) + u_2(a) = c

        Parameters
        ----------
        n_players
        """

        super().__init__(n_players)

