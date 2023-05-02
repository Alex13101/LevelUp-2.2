
'''Инкапсуляция'''

'''Для ограничения доступа к данным класса'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def _say(self):
        print(f'Hy, my name {self.name} and i am {self.__age} years old')

p = Person('John', 36)

print(p._say())

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age>0:
            self.__age=age

p = Person('John', 20)
print(p.age)
p.age =  -30
print(p.age)
