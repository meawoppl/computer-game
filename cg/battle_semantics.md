== Game Start ==

Each player must send a MakeMove rpc message to the game server
The sever will match opponents, and initialize the game state

The server will respond with a GameStatus message, describing the 
initial layout of the game.

Players must respond with a MakeMove message, which will be counted iff:
 - The answer is received within the ms_per_round time boundary
   as determined by the server
 - The move is valid as computed by the server
 - The game has not ended 

If any of the above are not satisfied by the submission of a client the server
will respond with the winning bitfeild for the opposing player in a message sent
to both parties.  Under this scenario, the opposing party will be credited with
a win.

If both parties fail to make a valid move, both parties
will be sent a loss message, and neither will be credited with a win.

When the game is won, the server will copy both players on the game state,
and end the stream (future messages will be ignored.)

