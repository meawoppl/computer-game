def isPlayLegal(stateVector, playVector):
    # Lets check the number of move allowed by this player
    movesToMake = stateVector.run()
    rightMoveCount = (playVector.sum() <= movesToMake)

    return rightMoveCount


def propagateState(stateVector, p1move, p2move):     # p1 is aiming for 0->1
    # p1 is aiming for 0->1
    # p2 is aiming for 1->0

    p1Feild = stateVector
    p2Feild = -stateVector

    p1Swaps = p1move & p2Feild
    p1Guess = p1move & p1Feild

    p2Swaps = p2move & p1Feild
    p2Guess = p2move & p2Feild

    p1Progress = p1Swaps & (-p2Guess)
    p2Progress = p2Swaps & (-p1Guess)

    totalProgress = p1Progress | p2Progress
    return stateVector ^ totalProgress
