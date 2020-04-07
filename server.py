import asyncio

class ServerProtocol:
    pass

class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = loop.create_server(
            0, '127.0.0.1', 8888
        )