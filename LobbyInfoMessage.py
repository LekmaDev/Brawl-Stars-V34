from Utils.Writer import Writer
import random
import time
from Utils.Helpers import Helpers

class LobbyInfoMessage(Writer):

    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        battles = Helpers.battles['BattlesCount']
        self.writeVint(self.count)
        self.writeString(f"GitHub: LekmaDev")

        self.writeVint(0) # array
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
