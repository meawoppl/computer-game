import importlib
import inspect
import os


from cg.players.abc import AbstractPlayer

_currentFolder = os.path.split(__file__)[0]


def findPlayers():
    # Poke through my directory looking for players
    thisDir = os.listdir(_currentFolder)

    players = {}
    for fileName in thisDir:
        modName = os.path.splitext(fileName)[0]
        if modName == "__init__":
            continue

        mod = importlib.import_module("cg.players." + modName)
        for objName in dir(mod):
            obj = getattr(mod, objName)
            if objName is "AbstractPlayer":
                continue
            if not inspect.isclass(obj):
                continue
            if not issubclass(obj, AbstractPlayer):
                continue
            players[objName] = obj

    return players
