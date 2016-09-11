from cg import rules


class AbstractBattle:
    def __init__(self, player1, player2, size=100):
        self.p1 = player1
        self.p2 = player2

        self.state = self.getStartingState()

        self.p1.opponent = self.p2.getName()
        self.p2.opponent = self.p1.getName()

        self.size = size

    def getPlayer1View(self):
        return self.gameState

    def getPlayer2View(self):
        return -self.gameState.reversed()

    def requestMoves(self):
        # Propogate the moves
        self.p1.state = self.getPlayer1View()
        self.p1.theirLast = -self.move.reversed()

        self.p2.state = self.getPlayer2View()
        self.p2.theirLast = -self.move.reversed()


        self.p1_last = p1.move()
        self.p2_last = p2.move()
        return self.p1_last, self.p2_last

    def propogateGame(self):
        p1Move, p2Move = requestMoves()
        self.gameState = rules.propagateState(self.gameState, p1Move, p2Move)


class InifinteBattle:
    def __init__(self):
        self.
    def run(self):


class FairBattle:
    def getStartingState(self):
        assert self.size % 2 == 0, "Fair battles only possible for even numbers"
        return 