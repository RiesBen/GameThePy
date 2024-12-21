import sympy as sp

from .normal_form_games import NormalFormGame


class CommonPayoffGames(NormalFormGame):

    def __init__(self, n_players:int):
        """
        Rule of the common payoff games is that all players gain the same payoff.
        also called Coordination Games, Team games.
        In these games there is no competition interest
        Extrem Situation - max coordination.

        Parameters
        ----------
        n_players
        """
        super().__init__(n_players=n_players)
        # There is one common payoff function for all players
        self.u = [sp.symbols('u') for i in range(n_players)]

