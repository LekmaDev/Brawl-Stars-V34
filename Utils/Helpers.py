import string
import random

class Helpers:
    connected_clients = {"ClientsCount": 0, "Clients": {}}
    battles = {"BattlesCount": 0}
    def randomToken(self):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self, length = 8):
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))

    def randomMapID(self):
        return random.randint(1, 2147483647)

