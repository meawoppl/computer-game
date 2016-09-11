import numpy as np
from cg.vector import Vector
from cg.players.abc import AbstractPlayer


class RandomAggressive(AbstractPlayer):
    """This player makes moves to expand its own territory."""
    def play(self):
        s = (-self.state).asarray()
        nz = np.nonzero(s)
        permuted = np.random.permutation(nz)[0: self.moveCount()]
        move = np.zeros(self.state.size)
        move[permuted] = 1
        return Vector(move)
