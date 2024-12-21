import numpy as np
import pandas as pd

class Game():
    def __init__(self, players, metric):
        self.players = players
        self.metric = metric


    def turn(self)->float:
        player_turn = np.array([p.decision() for p in self.players])
        return self.metric.draw(*player_turn)

    def turns(self, i:int=10):
        results = np.array([self.turn() for _ in range(i)])
        df = pd.DataFrame({"PlayerA": results[:, 0], "PlayerB": results[:, 1]})
        df.index += 1
        df.index.name = "Turn"
        return df
