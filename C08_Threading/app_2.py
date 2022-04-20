import random
import time
from socket import socket
from threading import Thread


def is_prime(number: int):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True
def primes(limit: int):
    time.sleep(random.randint(1, 3))
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    print(result)
    return result


class Client():
    def start(self) -> None:
        self.thd1 = Thread(target=primes, args=(200,))
        self.thd1.start()


class Server(Thread):
    pass


client = Client()
server = Server(target=primes, args=(100,))
client.start()
server.start()


network = socket()
network.bind(('localhost', 1500))
network.listen(1)
conn, addr = network.accept()
print(conn)
print(addr)