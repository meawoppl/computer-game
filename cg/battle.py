from cg import rules


class AbstractBattle:
    def __init__(self, startingState):
        self.gameState = startingState

    def getPlayer1View(self):
        return self.gameState

    def getPlayer2View(self):
        return -self.gameState.reversed()

    def move(self, p1, p2):
        p1Move = p1
        p2Move = p2.reversed()

        self.gameState = rules.propagateState(self.gameState, p1Move, p2Move)
