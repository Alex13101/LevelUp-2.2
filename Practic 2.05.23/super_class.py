''' Реализыция супер класса'''



class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self ,age):
        if age >0:
            self.__age =age

    def _say(self):
        print(f'Hy, my name {self.name} and i am {self.__age} years old')

class Child(Person):

    def __init__(self, name, age, toys):

        super().__init__(name, age) # Добавляем в класс данные предидущих классов и
                                    # их переменные

        self.toys =toys # Добавляем дополнительную переменную

    def play(self):
        print(f' im play in {self.toys}')



p = Person('John', 20)
print(p.age)
p.age =  -30
print(p.age)
c= Child('Jack', 5, 'car')
c._say()
c.play()


class NweStr(str):    #Магические методы __sub__(разность)

    def __sub__(self, other):
        obj = self.replace(other, '')
        return obj


s1 = NweStr('Hello world')
s2 = NweStr('world')

s3 = s1-s2
s4 = s1.__sub__(s2)
print(s1 + s2)
print(s3)
print(s4)