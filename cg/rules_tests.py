import numpy as np

from cg.vector import Vector, random
from cg import rules


def test_nullPlayLegality():
    """Make sure null play is allowed"""
    for _n in range(50):
        stateVector = random(50, 0.5)

        # Null play is _always_ legal!
        pv = Vector(np.zeros(50))
        assert rules.isPlayLegal(stateVector, pv), "Null play comes back as illegal :("


def test_singlePlay():
    """Make sure each player will play"""
    playSize = 50
    for n in range(playSize):
        s = np.zeros(playSize)
        s[n] = 1
        sv = Vector(s)

        p = np.zeros(playSize)
        p[0] = 1
        pv = Vector(p)

        assert rules.isPlayLegal(sv, pv)


def test_tiny_game_complete():
    """Sanity check all the legal moves of a small game"""

    beginState = Vector((0, 1))
    noMove = Vector((0, 0))

    # No one moves
    nextState = rules.propagateState(beginState, noMove, noMove)
    assert beginState == nextState

    # Only player 1 Moves (offence) -> win for p1
    nextState = rules.propagateState(beginState, Vector((1, 0)), noMove)
    assert nextState == Vector((1, 1))

    # Only player 1 Moved (defense) -> NC
    nextState = rules.propagateState(beginState, Vector((0, 1)), noMove)
    assert nextState == beginState

    # Only player 2 moves (offence) -> win for p2
    nextState = rules.propagateState(beginState, noMove, Vector((0, 1)))
    assert nextState == Vector((0, 0))

    # Only player 2 moved (defence) -> NC
    nextState = rules.propagateState(beginState, noMove, Vector((1, 0)))
    assert nextState == beginState

    # p1 and p2 both make complimentary moves (off/def) -> NC
    m1 = Vector((0, 1))
    nextState = rules.propagateState(beginState, m1, m1)
    assert nextState == beginState

    m2 = Vector((1, 0))
    nextState = rules.propagateState(beginState, m2, m2)
    assert nextState == beginState

    # Both attack (all bits flipped!)
    nextState = rules.propagateState(beginState, Vector((1, 0)), Vector((0, 1)))
    assert nextState == Vector((1, 0))

    # Both defend (no bits flipped)
    nextState = rules.propagateState(beginState, Vector((0, 1)), Vector((1, 0)))
    assert nextState == Vector((0, 1))
