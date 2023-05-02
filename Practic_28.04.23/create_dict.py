lst = [1, 2, 3, 4, -5, 6, 7, 8, 9]

new_list = {el: el ** 2 for el in lst}
print(new_list)
for k, v in new_list.items():
   print(f' Квадрат числа {k} равен  {v}')


def func_1():
   print('Функция 1')

def func_2():
   print('Функция 2')

def func_3():
   print('Функция 3')


switcher = {
   1: func_1,
   2: func_2,
   3: func_3
}

def switch(case):
   func = switcher.get(case, lambda: print('Неверный выбор'))
   func()

switch(int(input('Введите номер функции: '))) # Выводит функию 1
switch(2) # Выводит функию 2
switch(1) # Выводит Неверный выбор