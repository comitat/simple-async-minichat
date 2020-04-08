import asyncio
from asyncio import transports

class ClientProtocol(asyncio.Protocol):
    transport: transports.Transport
    window: 'MainWindow'

    def __init__(self, chat_window: 'MainWindow'):
        self.window = chat_window

    def data_received(self, data: bytes):
        decoded = data.decode()
        self.window.append_text(decoded)

    def send_data(self, message: str):
        encoded = message.encode()
        self.transport.write(encoded)

    def connection_made(self, transport: transports.Transport):
        self.window.append_text("Online")
        self.transport = transport

    def connection_lost(self, exception):
        self.window.append_text("Offline")

class MainWindow(QMainWindow, Ui_MainWindow):
    protocol: ClientProtocol

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.message_button.clicked.connect(self.button_handler)
