class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self._age = value

person = Person("John", 30)
print(person.name)  # Выводит "John"
person.name = "Jack"
print(person.name)  # Выводит "Jack"
print(person.age)  # Выводит "30"
person.age = 35
print(person.age)  # Выводит "35"


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.6f}s")
        return result
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()



import random
import time

def retry(num_retries=5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Exception: {e}. Retrying...")
                    time.sleep(random.uniform(0, 1))
            raise Exception(f"Function {func.__name__} failed after {num_retries} retries")
        return wrapper
    return decorator

@retry()
def my_function():
    if random.random() < 0.8:
        raise Exception("Something went wrong")
    else:
        return "Success"

result = my_function()
print(result)