import re


class Book:
    pattern = '^(?P<increment>#{1,3})\s+(?P<chapter>.+)'
    def __init__(self, filename):
        with open(filename, 'r') as filename:
            self.filename = filename.read()

    def print_book(self):
        print(self.filename)

    def make_chapters(self):
        for line in self.filename.splitlines():
            match = re.search(self.pattern, line)
            if match:
                print(f"{match.group('increment')} {match.group('chapter')}")


book = Book('text.md')
# book.print_book()
book.make_chapters()
