import argparse

import cg.players

# Snoop the players file for available scripts
players = cg.players.findPlayers()
playerNames = list(players.keys())


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('player1', choices=playerNames,
                    help='Selection for player 1')
parser.add_argument('player2', choices=playerNames,
                    help='Selection for player 2')

args = parser.parse_args()

player1class = players[args.player1]
player2class = players[args.player2]
