from Utils.Reader import Reader
from Protocol.Messages.Server.Gameroom.TeamStream import TeamStream

class TeamPremadeChatMessage(Reader):
	#14369
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player = player
		
	def decode(self):
		print(f"[INFO] TeamPremadeChatMessage send! Pin: {self.readVint()} Mode: {self.player.mode}")
		self.player.pin = self.readVint()
		self.player.mode = self.readVint()
		 
	def process(self):
		#self.player.pin = self.pin
		self.player.tick += 1
		TeamStream(self.client, self.player).send()