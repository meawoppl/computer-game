from cg.vector import zeros
from cg.players.abc import AbstractPlayer


class NullPlayer(AbstractPlayer):
    """This player is basically a goldfish.
    It never makes a move and accepts fate
    as it comes."""
    def play(self):
        return zeros(self.state.size)
