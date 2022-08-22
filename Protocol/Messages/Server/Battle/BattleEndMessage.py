from Utils.Writer import Writer
from Utils.Helpers import Helpers


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players

    def encode(self):
        self.writeVint(self.type)
        self.writeVint(self.result)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(0)
        self.writeVint(32)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                self.writeVint(player) if self.team == 0 else self.writeVint(2)
            else:
                self.writeVint(2 if self.team != 0 else 1) if self.type == 2 else self.writeVint(self.team if self.team != 1 else 2)

            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVint(0)
            self.writeDataReference(29, self.skin)   if self.skin != -1 else self.writeVint(0)

            self.writeVint(0) # Brawler Trophies
            self.writeVint(0) # Power Play Points
            self.writeVint(10) # Brawler Power Level

            self.writeBool(False)

            # sub_64DF74
            self.writeString(self.username)
            self.writeVint(100)
            self.writeVint(28000000)
            self.writeVint(43000000 + self.player.nameColor)
            if self.player.bp_activated == 1:
            	self.writeVint(46000000 + self.player.nameColor)
            else:
                self.writeNullVint()


        self.writeBool(False)
        self.writeBool(False)
        self.writeBool(False)

        self.writeDataReference(28, 0)

        self.writeBool(False)
        
        Helpers.battles['BattlesCount'] += 1
        
        # Trophies #
        # 3 vs 3 #
        if self.type == 0 and self.result == 0:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 8
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 8
        	self.player.trophies += 8
        if self.type == 0 and self.result == 1:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] -= 2
        	self.player.trophies -= 2
        	
        # Showdown #
        if self.type == 2 and self.result == 1:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 10
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 10
        	self.player.trophies += 10
        if self.type == 2 and self.result == 2:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 8
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 8
        	self.player.trophies += 8
        if self.type == 2 and self.result == 3:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 7
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 7
        	self.player.trophies += 7
        if self.type == 2 and self.result == 4:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 6
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 6
        	self.player.trophies += 6
        if self.type == 2 and self.result == 5:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 3
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 3
        	self.player.trophies += 3
        if self.type == 2 and self.result in [6,7]:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 2
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 2
        	self.player.trophies += 2
        if self.type == 2 and self.result == 9:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] -= 1
        	self.player.trophies -= 1
        if self.type == 2 and self.result == 10:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] -= 2
        	self.player.trophies -= 2
        	
        # Duo Showdown #
        if self.type == 5 and self.result == 1:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 9
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 9
        	self.player.trophies += 9
        if self.type == 5 and self.result == 2:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 7
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 7
        	self.player.trophies += 7
        if self.type == 5 and self.result == 3:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] += 4
        	self.player.brawlers_high_trophies[str(self.player.homeBrawler)] += 4
        	self.player.trophies += 4
        if self.type == 5 and self.result == 5:
        	self.player.brawlers_trophies[str(self.player.homeBrawler)] -= 1
        	self.player.trophies -= 1
        self.player.updateAccount('Trophies', self.player.trophies)
        self.player.updateAccount('brawlers_trophies', self.player.brawlers_trophies)
        self.player.updateAccount('brawlers_high_trophies', self.player.brawlers_high_trophies)

