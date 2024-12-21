import random

class Player():
    def __init__(self):
        pass

class MixedStrategy(Player):
    def __init__(self):
        pass

class PureStrategy(Player):
    def __init__(self):
        pass


class RandomStrategyPlayer(Player):

    def __init__(self):
        """
            Also Called Mixed Strategy

        """
        pass

    def decision(self):
        return random.getrandbits(1)


class PureStrategyPlayer(Player):

    def __init__(self, strategy):
        self.strategy = strategy

    def decision(self):
        return self.action