import numpy as np
from cg.vector import Vector
from cg.players.abc import AbstractPlayer


class Random(AbstractPlayer):
    """This player is basically a goldfish.
    It never makes a move and accepts fate
    as it comes."""
    def play(self):
        chooseFrom = np.arange(self.state.size, dtype=np.uint32)
        permuted = np.random.permutation(chooseFrom)
        move = np.zeros(self.state.size)
        move[permuted[0: self.moveCount()]] = 1
        return Vector(move)
