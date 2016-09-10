import hashlib


class AbstractPlayer:
    def __init__(self):
        """Abstract base class for a game player."""
        # These variables are what .setup() and .run() can use
        # to prepate and play against another player!
        self.opponent = None
        self.move = 0
        self.state = None
        self.myLastMove = None
        self.theirLastMove = None

    def getName(self):
        name = self.__class__.__name__
        s = hashlib.sha1()
        s.update(self.setup.__code__.co_code)
        s.update(self.play.__code__.co_code)
        return name + "-" + s.hexdigest()[::4]

    def moveCount(self):
        """Return the number of move I get to make this turn"""
        return self.state.run()

    def setup(self):
        """
        This is the time that the player can do static setup.
        This time is not clocked, and occurs before gameplay can begin.
        """
        pass

    def play(self):
        """This method defines the player."""
        raise NotImplemented("Users must implement this.")

    def teardown(self):
        """Mirror function to setup() use to close ports or cleanup etc."""
