class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @staticmethod
    def _say(self):
        print(f'Hy, my name {self.name} and i am {self.__age} years old')


p = Person('John', 36)
c = Person('Jack', 20)

Person._say(p)
Person._say(c)
