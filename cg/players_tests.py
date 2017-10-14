from cg.vector import Vector, random, zeros
from cg.players import findPlayers


def test_findPlayers():
    """Find seemingly valid players"""
    assert len(findPlayers()) > 0, "No players found?"


def test_playerSignatures():
    """Check all player methods."""
    for player_name, player in findPlayers().items():
        assert hasattr(player, "setup")
        assert hasattr(player, "play")


def test_initAllPlayers():
    """Make sure init passes for all players"""
    for player_name, player in findPlayers().items():
        player()


def test_getNullMove():
    """Make sure players know at least 1 rule."""
    null_vec = zeros(10)
    for player_name, player in findPlayers().items():
        p = player()
        p.setup()
        print("Testing Player:" + p.getName())
        p.opponent = "YourWorstEnemy"
        p.move = 0
        p.myLastMove = null_vec
        p.theirLastMove = null_vec
        p.state = null_vec

        # All players should recognise this situation as a loss and return a zero vector
        r = p.play()
        assert r == null_vec, str(r)

        p.teardown()


def test_getRandomResponse():
    """Give players a random feild and see what they do"""
    null_vec = zeros(1000)
    random_state = random(1000, 0.5)
    for playername, player in findPlayers().items():
        p = player()
        p.setup()
        print("Testing Player:" + p.getName())
        p.opponent = "YourWorstEnemy"
        p.move = 0
        p.myLastMove = null_vec
        p.theirLastMove = null_vec
        p.state = random_state

        # players shouldnt crash, and return a  Vector
        r = p.play()
        assert isinstance(r, Vector)
