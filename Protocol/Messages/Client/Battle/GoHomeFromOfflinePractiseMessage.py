from Protocol.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Utils.Reader import Reader


class GoHomeFromOfflinePractiseMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        OwnHomeDataMessage(self.client, self.player).send()