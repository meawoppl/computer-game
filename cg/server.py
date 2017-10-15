from concurrent import futures

import grpc

import cg.gameplay_pb2 as msgs
import cg.gameplay_pb2_grpc as server_stub


class InvalidPlayException(RuntimeError):
    pass


RANDOM_GAME_SIZE = (2**4, 2**6, 2**8, 2**10)




class GameServer(server_stub.GameServerServicer):
    def PlayGame(self, incoming_iter, context):
        # Send the initial game status
        initial_message = next(incoming_iter)
        assert initial_message.player_id is not ""

        find_waiting_game()

        yield msgs.GameStatus()
        print(context, dir(context))
        raise InvalidPlayException("Testing")

        for play in incoming_iter:
            print("Server Got:", type(play))
            yield msgs.GameStatus()

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
server_stub.add_GameServerServicer_to_server(GameServer(), server)
print("Bound Port:", server.add_insecure_port('[::]:50051'))
server.start()

channel = grpc.insecure_channel("localhost:50051")
channel.subscribe(lambda status: print("Channel Status Callback:", status))
stub = server_stub.GameServerStub(channel)


def GameClient:
    def __init__(self, client_name, game_server_stub):
        self._name = client_name
        self._stub = game_server_stub

    def play_game(self, call) -> bool:
        """
        call must have the signature
        call(game_status) -> [bool]

        returns a boolean as to whether you have won
        """
        assert callable(call), call

        def _play_callback(self, status_iterator)
            # Send the initial data about the player to the server
            yield msgs.MakeMove(player_id=self._name)

            for state in gamestate:
                my_move = call(status_iterator)
                move_msg = msgs.MakeMove()
                move_msg.player_id = self._name
                move_msg.round = gamestate.round
                move_msg.move.bits.extend(my_move)

        for mov in self._stub.PlayGame(_play_callback):
            print(mov)
            # Victory/loss exit criteria here


    def _start_game(self):
        return  



def encode_move(bools):
    for b in bools:
        assert isinstance(b, bool)
    bv = msgs.BooleanVector()
    bv.bits.extend(bools)
    return bv


def decode_vector(msg_bits):
    return np.array(msg_bits, dtype=np.bool)

def send_iterator():
    yield 
    while True:
        yield msgs.MakeMove()

game = stub.PlayGame(send_iterator())

for response in game:
    print("Resp:", type(response))
