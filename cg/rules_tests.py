import numpy as np

from cg.vector import Vector, random
from cg import rules


def test_nullPlayLegality():
    """Make sure null play is allowed"""
    for _n in range(50):
        state_vector = random(50, 0.5)

        # Null play is _always_ legal!
        pv = Vector(np.zeros(50))
        assert rules.isPlayLegal(state_vector, pv), "Null play comes back as illegal :("


def test_singlePlay():
    """Make sure each player will play"""
    play_size = 50
    for n in range(play_size):
        s = np.zeros(play_size)
        s[n] = 1
        sv = Vector(s)

        p = np.zeros(play_size)
        p[0] = 1
        pv = Vector(p)

        assert rules.isPlayLegal(sv, pv)


def test_tiny_game_complete():
    """Sanity check all the legal moves of a small game"""

    begin_state = Vector((0, 1))
    no_move = Vector((0, 0))

    # No one moves
    next_state = rules.propagateState(begin_state, no_move, no_move)
    assert begin_state == next_state

    # Only player 1 Moves (offense) -> win for p1
    next_state = rules.propagateState(begin_state, Vector((1, 0)), no_move)
    assert next_state == Vector((1, 1))

    # Only player 1 Moved (defense) -> NC
    next_state = rules.propagateState(begin_state, Vector((0, 1)), no_move)
    assert next_state == begin_state

    # Only player 2 moves (offense) -> win for p2
    next_state = rules.propagateState(begin_state, no_move, Vector((0, 1)))
    assert next_state == Vector((0, 0))

    # Only player 2 moved (defense) -> NC
    next_state = rules.propagateState(begin_state, no_move, Vector((1, 0)))
    assert next_state == begin_state

    # p1 and p2 both make complimentary moves (off/def) -> NC
    m1 = Vector((0, 1))
    next_state = rules.propagateState(begin_state, m1, m1)
    assert next_state == begin_state

    m2 = Vector((1, 0))
    next_state = rules.propagateState(begin_state, m2, m2)
    assert next_state == begin_state

    # Both attack (all bits flipped!)
    next_state = rules.propagateState(begin_state, Vector((1, 0)), Vector((0, 1)))
    assert next_state == Vector((1, 0))

    # Both defend (no bits flipped)
    next_state = rules.propagateState(begin_state, Vector((0, 1)), Vector((1, 0)))
    assert next_state == Vector((0, 1))
