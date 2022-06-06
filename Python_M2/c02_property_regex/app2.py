import re


class Book:
    pattern = "^(?P<INC>#{1,3})\s+(?P<CHP>.+)"

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.file = file.read()

    def print_book(self):
        print(self.file)

    def make_chapters(self):
        c = 0
        cc = 0
        ccc = 0
        for line in self.file.splitlines():
            match = re.search(self.pattern, line)
            if match:
                if len(match.group('INC')) == 1:
                    c += 1
                if len(match.group('INC')) == 2:
                    cc += 1
                if len(match.group('INC')) == 3:
                    ccc += 1
                print(f'{c}.{cc}.{ccc} {match.group("CHP")}')


book = Book('text.md')
book.print_book()
book.make_chapters()
