from Protocol.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage
from Utils.Reader import Reader


class KeepAliveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.client, self.player).send()