from Utils.Writer import Writer

class TeamStream2(Writer):

    def __init__(self, client, player, message):
        super().__init__(client)
        self.id = 24131
        self.player = player
        self.message = message

    def encode(self):
        self.writeVint(0) # High ID
        self.writeVint(self.player.room_id) # Room ID
        self.writeVint(1) # ?
        for i in range(1):
            self.writeVint(2) # Event?
            self.writeVint(0)
            self.writeVint(self.player.tick) # tick
            self.writeVint(0)  # High ID
            self.writeVint(self.player.low_id)  # Low ID
            self.writeString(self.player.name) # Player name
            self.writeVint(0)
            self.writeVint(0) # Age Seconds (TID_STREAM_ENTRY_AGE)
            self.writeVint(0) # Boolean
            self.writeString(self.message) # Message