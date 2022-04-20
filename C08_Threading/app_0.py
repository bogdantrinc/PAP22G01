from threading import Thread


def write_to_file(message: str):
    with open('my_file', 'a') as file:
        file.write(f'My test in thread: {message}\n')

for _ in range(100):
    thread = Thread(target=write_to_file, args=(str(_),))
    thread.start()