import re


class Rank:
    def __init__(self, string, rank):
        self.string = string
        self.rank = rank


class Book:
    pattern = r'^(?P<increment>#{1,3})\s+(?P<chapter>.+)'

    def __init__(self, filename):
        with open(filename, 'r') as filename:
            self.filename = filename.read()

    def print_book(self):
        print(self.filename)

    def make_chapters(self):
        list = []
        for line in self.filename.splitlines():
            match = re.search(self.pattern, line)
            if match:
                # print(f"{match.group('increment')} {match.group('chapter')}")
                list.append(Rank(match.group('chapter'), len(match.group('increment'))))
        for i in range(len(list)):
            print(list[i].rank, list[i].string)


book = Book('text.md')
# book.print_book()
book.make_chapters()
