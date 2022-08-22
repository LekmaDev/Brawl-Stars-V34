from Utils.Writer import Writer

class LatencyTestResultMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 29903
        self.player = player

    def encode(self):
    	self.writeVint(1)
    	self.writeVint(1)
    	self.writeVint(1)
    	self.writeVint(1)
    	self.writeVint(1)
    	self.writeVint(1)
    	self.writeVint(1)
    	self.writeBoolean(True)
    	self.writeString("а там да")