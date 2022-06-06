# example
file = open('text', 'w')
file.write('string')
file.close()

with open('text', 'r') as file:
    print(file.readline())


# new class context manager
class FileOpener(object):
    def __init__(self, path, mode):
        self.my_file = open(path, mode)

    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        print('in exit')
        self.my_file.close()
        if exc_type == AttributeError:
            return True


    def writ_text(self, text):
        self.my_file.write(text)

with FileOpener('text', 'w') as new_file:
    new_file.writ_text('my text')
    new_file.writ_text2('my text')



print(80*"#")
from contextlib import contextmanager

@contextmanager
def file_opener(path, mode):
    my_file = open(path, mode)
    try:
        print('in enter')
        yield my_file
    except AttributeError:
        print('we have an exception')
    finally:
        print('in exit')
        my_file.close()

with file_opener('text', 'w') as new_file:
    new_file.writ_text('my text2')