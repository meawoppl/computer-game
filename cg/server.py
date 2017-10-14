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
server_stub.add_GameServerServicer_to_server(
    GameServer(), server)
print("Bound Port:", server.add_insecure_port('[::]:50051'))
server.start()

channel = grpc.insecure_channel("localhost:50051")
channel.subscribe(lambda status: print("Channel Status Callback:", status))
stub = server_stub.GameServerStub(channel)


def send_iterator():
    yield msgs.MakeMove(player_id="FooPlayer")
    while True:
        yield msgs.MakeMove()

game = stub.PlayGame(send_iterator())

for response in game:
    print("Resp:", type(response))
