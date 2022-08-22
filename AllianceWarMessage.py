from Utils.Writer import Writer


class AllianceWarMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24776
        self.client = client
        self.player = player


    def encode(self):
        self.writeInt(0) # Player ID
        self.writeInt(1) # Player ID
        self.writeVint(0) # Your Club Faction
        

        # Club War Events Array
        self.writeVint(0) # Count
        for x in range(0):
            self.writeVint(x)
        # Club War Events Array End
        

        # Club War Factions Array
        self.writeVint(0) # Count
        for x in range(0):
            self.writeVint(x)
        # Club War Factions Array End