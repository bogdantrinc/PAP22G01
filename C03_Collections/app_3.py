"""
Create a self organising and self sorting phonebook
 - adding new users will keep dictionary order
 - removing users will preserve order
"""
from collections import OrderedDict


class PhoneBook():
    agenda = OrderedDict()

    def add_contact(self, name, number):
        self.agenda[name] = number
        for key in list(self.agenda.keys()):
            if key > name:
                self.agenda.move_to_end(key)

    def remove_number(self, number):
        for i, j in self.agenda.copy().items():
            if j == number:
                del self.agenda[i]  # self.agenda.pop(i) - cu pop poti returna intr-o variabila elemetul pe care il scoti
    def list_users(self,name):
        for n,nr in self.agenda.items():
            if name.lower() in n.lower():
                print("Nume:",n,"Numar:",nr)

phone_book = PhoneBook()
phone_book.add_contact("Marcel", "1234")
phone_book.add_contact("Ana", "5678")
phone_book.add_contact("Daniel", "5678")
phone_book.add_contact("Mihai", "5678")
phone_book.remove_number("5678")
phone_book.list_users("mar")
print(phone_book.agenda)

