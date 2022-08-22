from Utils.Writer import Writer
from Logic.EventSlots import EventSlots
from Logic.Shop import Shop


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        # sub_4558EC #
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(self.player.trophies)
        self.writeVint(self.player.trophies)
        self.writeVint(self.player.trophies)

        self.writeVint(200)   # Trophy Road Reward
        self.writeVint(99999) # Exp Points

        self.writeDataReference(28, self.player.thumbnail)
        self.writeDataReference(43, self.player.nameColor)

        self.writeVint(0)
        for x in range(0):
            self.writeVint(x)

        # Selected Skins array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeDataReference(29, self.player.brawlers_skins[brawler_id] )

        # Unlocked Skins array
        self.writeVint(len(self.player.skinsID))
        for skin_id in self.player.skinsID:
            self.writeDataReference(29, 0)

        self.writeVint(0)
        for x in range(0):
            self.writeDataReference(29, 0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(99999) # Trophy League End Timer
        self.writeVint(99999)
        self.writeVint(99999) # Season End Timer

        self.writeVint(0)

        self.writeBool(False)
        self.writeBool(False)

        self.writeUInt8(4)

        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)

        self.writeVint(0)   # Name Change Cost
        self.writeVint(0)   # Name Change Timer

        # Shop Array
        Shop.EncodeShopOffers(self)
        # Shop Array End

        # sub_1F09D8
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # array
        for x in range(0):
            self.writeVint(x)

        self.writeVint(1)  # Tickets
        self.writeVint(1)

        self.writeDataReference(16, 0)

        self.writeString("RU")
        self.writeString("Bild Team")

        # sub_587CF4
        self.writeVint(0)
        for x in range(0):
            self.writeInt(0)
            self.writeInt(0)

        # sub_4505B4
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeDataReference(0, 0)
            self.writeVint(0)

        # Brawl Pass Array
        self.writeVint(1)
        for x in range(1):
            self.writeVint(4)  # Current Season
            self.writeVint(-1)  # Pass Tokens
            self.writeUInt8(self.player.bp_activated) # Brawl Pass Activated
            self.writeVint(0)  # Pass Progress

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)

        # sub_67CBFC
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)

        # Quests Array
        self.writeBoolean(True)
        if True:
            self.writeVint(1)
            for x in range(1):
                self.writeVint(0)     # Unknown
                self.writeVint(0)     # Unknown
                self.writeVint(1)     # Mission Type
                self.writeVint(2)     # Achieved Goal
                self.writeVint(8)     # Quest Goal
                self.writeVint(10)    # Tokens Reward
                self.writeVint(0)     # Unknown
                self.writeVint(0)     # Current level
                self.writeVint(0)     # Max level
                self.writeVint(1)     # Quest Type
                self.writeUInt8(2)    # Quest State
                self.writeDataReference(16, 0) # Brawler SCID
                self.writeVint(0)     # GameMode
                self.writeVint(0)     # Unknown
                self.writeVint(0)     # Unknown

        # Emotes Array
        self.writeBoolean(True)
        if True:
            self.writeVint(len(self.player.emotesID))
            for emote_id in self.player.emotesID:
                self.writeDataReference(52, emote_id)
                self.writeVint(1)     # Unknown
                self.writeVint(1)     # Unknown
                self.writeVint(1)     # Unknown


        # sub_2CEABC #
        self.writeVint(0)   # Shop Timestamp
        self.writeVint(100) # Tokens for Brawl Box
        self.writeVint(10)  # Tokens for Big Box

        for item in Shop.boxes:
            self.writeVint(item['Cost'])
            self.writeVint(item['Multiplier'])

        self.writeVint(Shop.token_doubler['Cost'])
        self.writeVint(Shop.token_doubler['Amount'])

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0)

        # LOGIC EVENTS #

        # sub_21D148
        count = len(EventSlots.maps)
        self.writeVint(count + 1)
        for i in range(count + 1):
            self.writeVint(i)

        # sub_359438
        self.writeVint(count)
        for map in EventSlots.maps:
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)

            self.writeVint(map['Ended'])
            self.writeVint(map['Timer'])
            self.writeVint(0)
            self.writeDataReference(15, map['ID'])
            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeBoolean(False)
            self.writeVint(0)
            self.writeVint(0)

         # sub_359438
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeDataReference(15, 0)
            self.writeVint(0)
            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeBoolean(False)
            self.writeVint(0)
            self.writeVint(0)

        # 6 x sub_3DC00C
        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])
        self.writeArrayVint([1, 2, 3, 4, 5, 10, 15, 20])
        self.writeArrayVint([10, 30, 80])
        self.writeArrayVint([6, 20, 60])
        self.writeArrayVint([20, 50, 140, 280])
        self.writeArrayVint([150, 400, 1200, 2600])

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeUInt8(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeUInt8(1)

        # sub_1D0FA4
        self.writeVint(0)
        for x in range(0):
            self.writeDataReference(0, 0)
            self.writeInt(0)
            self.writeInt(0)

        # sub_587CF4
        self.writeVint(1)
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000022)

        # sub_6190D0
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)

            # 3 x sub_34DCDC
            for x in range(3):
                self.writeInt(0)
                self.writeStringReference('')

        self.writeLong(self.player.ID)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(0)
        self.writeUInt8(0)

        bool = False
        self.writeBool(bool)
        if bool:
            self.writeVint(0)
            # sub_5A01C0
            for x in range(0):
                self.writeVint(0)
                self.writeDataReference(0, 0)
                self.writeVint(0)
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)

        self.writeVint(0)
        for x in range(0):
            self.writeDataReference(0, 0)

        self.writeLogicLong(self.player.ID)
        self.writeLogicLong(self.player.ID)
        self.writeLogicLong(self.player.ID)

        self.writeString(self.player.name)
        self.writeBool(self.player.Data['NameSet'])

        self.writeInt(0)

        # Commodity count
        self.writeVint(8)

        # Unlocked Brawlers & Resources array
        self.writeVint(len(self.player.cardsUnlockID) + len(self.player.Data['Resources']))
        for unlock_id in self.player.cardsUnlockID:
            self.writeVint(23)
            self.writeVint(unlock_id)
            self.writeVint(1)
        for resource in self.player.Data['Resources']:
            self.writeDataReference(5, resource['ID'])
            self.writeVint(resource['Amount'])

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies[str(brawler_id)])

        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(self.player.brawlers_high_trophies[str(brawler_id)])

        self.writeVint(0)

        # Brawlers Upgrade Poitns array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(0)

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(8)

        # Gadgets and Star Powers array
        self.writeVint(len(self.player.cardsSkillsID))
        for skill_id in self.player.cardsSkillsID:
            self.writeVint(23)
            self.writeVint(skill_id)
            self.writeVint(1)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(self.player.gems)
        self.writeVint(self.player.gems)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2) # Tutorial Step
        self.writeVint(0)


