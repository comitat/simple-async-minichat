import asyncio

class ServerProtocol (asyncio.Protocol):
    login : str
    server : 'Server'

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        print(data)

    def connection_made(self, transport: transports.Transport):
        print ("OK")
    
    def connection_lost(self, exception):
        print("Lost")


class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol, '127.0.0.1', 8888
        )

    print ("Server Start")

    await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Server stoped")