print("Private server created by Lekma and vanya_dev")

import socket
import time
from threading import *

from Logic.Device import Device
from Logic.Player import Player
from Protocol.LogicMessageFactory import packets
from LobbyInfoMessage import LobbyInfoMessage
from Utils.Helpers import Helpers


def _(*args):
	print('[INFO]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()

class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		self.server.bind((self.ip, self.port))
		_(f'Server started! Ip: {self.ip}, Port: {self.port}')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			_(f'New connection! Ip: {address[0]}')
			ClientThread(client, address).start()
			Helpers.connected_clients['ClientsCount'] += 1
			
class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Player(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("ERROR while receiving data!")
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		while True:
			header = self.client.recv(7)
			if len(header) > 0:
				last_packet = time.time()
				packet_id = int.from_bytes(header[:2], 'big')
				length = int.from_bytes(header[2:5], 'big')
				data = self.recvall(length)

				if packet_id in packets:
					_(f'Received packet! Id: {packet_id}')
					message = packets[packet_id](self.client, self.player, data)
					message.decode()
					message.process()
				else:
					_(f'Packet not handled! ({packet_id})')
				LobbyInfoMessage(self.client, self.player, Helpers.connected_clients['ClientsCount']).send()
			if time.time() - last_packet > 10:
				_("Client disconnected!")
				self.client.close()
				Helpers.connected_clients['ClientsCount'] -= 1
				break
				
if __name__ == '__main__':
	server = Server('0.0.0.0', 9339)
	server.start()
