import numpy as np
import sympy as sp

class NormalFormGame():

    def __init__(self, n_players):
        # All Players in the vector N. indexed with i
        self.N = [sp.Symbol(f"p_{i}") for i in range(n_players)]
        # All sets of possible actions. Each action vector is an action profile. A=(A_1 x ... x A_N)
        self.A = [sp.Symbol(f"a_{i}") for i in range(n_players)]
        # Where u_i: A->R  = real-valued utility (payoff function)
        self.u = [sp.Symbol(f"u_{i}") for i in range(n_players)]
        