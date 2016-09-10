from cg.vector import Vector, random, zeros
from cg.players import findPlayers


def test_findPlayers():
    """Find seemingly valid players"""
    assert len(findPlayers()) > 0, "No players found?"


def test_playerSignatures():
    """Check all player methods."""
    for player in findPlayers():
        assert hasattr(player, "setup")
        assert hasattr(player, "play")


def test_initAllPlayers():
    for player in findPlayers():
        player()


def test_getNullMove():
    nullVec = zeros(10)
    for player in findPlayers():
        p = player()
        p.setup()
        print("Testing Player:" + p.getName())
        p.opponent = "YourWorstEnemy"
        p.move = 0
        p.myLastMove = nullVec
        p.theirLastMove = nullVec
        p.state = nullVec

        # All players should recognise this situation as a loss and return a zero vector
        r = p.play()
        assert r == nullVec, str(r)

        p.teardown()


def test_getRandomResponse():
    nullVec = zeros(1000)
    randomState = random(1000, 0.5)
    for player in findPlayers():
        p = player()
        p.setup()
        print("Testing Player:" + p.getName())
        p.opponent = "YourWorstEnemy"
        p.move = 0
        p.myLastMove = nullVec
        p.theirLastMove = nullVec
        p.state = randomState

        # players shouldnt crash, and return a  Vector
        r = p.play()
        assert isinstance(r, Vector)
