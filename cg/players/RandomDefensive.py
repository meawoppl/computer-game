import numpy as np
from cg.vector import Vector
from cg.players.abc import AbstractPlayer


class RandomDefensive(AbstractPlayer):
    """This player is basically a goldfish.
    It never makes a move and accepts fate
    as it comes."""
    def play(self):
        s = (self.state).asarray()
        nz = np.nonzero(s)
        permuted = np.random.permutation(nz)[0: self.moveCount()]
        move = np.zeros(self.state.size)
        move[permuted] = 1
        return Vector(move)
