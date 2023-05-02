# Полиморфизм'''

'''Использование классов паралельно и не зависимо друг от друга'''
class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def __len__(self):
        return self.__age

p = Person('John', 20)

print(len(p))