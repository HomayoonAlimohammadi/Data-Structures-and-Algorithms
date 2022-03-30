import random 
import re

class Person:
    idx = []
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self._email = f'{first}.{last}@gmail.com'
        self._id = random.randrange(1000,10000)
    
    @property
    def email(self):
        # self._email = f'{self.first}.{self.last}@gmail.com'
        return self._email

    @email.setter
    def email(self, new_email):
        match = re.search(r'^[a-zA-Z]+[a-zA-Z0-9.]*\@[a-zA-Z]+\.[a-zA-Z]+$', new_email)
        if match:
            self._email = new_email
        else:
            print('Invalid Email.')

    @email.deleter
    def email(self):
        self._email = None

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'''{self.first} {self.last}
{self._email}
{self.id}'''



random.seed(0)
person = Person('homayoon', 'alimohammadi')
print(person)
print(person.email)
person.first = 'nooshin'
print(person)
print(person.email)
print(person.id)
person.email = 'h.a@gmail.com'
print(person.email)
del person.email
print(person)