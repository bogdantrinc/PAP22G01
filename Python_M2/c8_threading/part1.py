import socket
from threading import Thread


def write_to_file1(message: str):
    with open('my_file', 'a') as file:
        file.write(f'My test in thread: {message}')


for i in range(100):
    thread = Thread(target=write_to_file1, args=(str(i),))
    thread.start()

network = socket.socket()
network.bind(('localhost', 1500))
network.listen(1)
conn, addr = network.accept()
print(conn)
print(addr)