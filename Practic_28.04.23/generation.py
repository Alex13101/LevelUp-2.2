
'''Генераторы чисел'''


lst = [-1, 2, 3, 4, -5, 6, 7, 8, 9]

def square (x):
    return x**2


list = [x**2 for x in lst] # Итерируемые объекты в генераторе

print(list, '\n')
print(*list) # Знак звездочка показывает объект генерации
print(*list) # В таком выражении (list = (x**2-1 for x in lst)) может вызываться много раз


def my_generations(l = 1_000):
    i = 0
    while i < l:
        yield i
        i+=1
lst = my_generations() # тут вызывается один раз после чего стирается и остается пустым
new_list = []
for i in lst:
    new_list.append(i**2) # Квадрат чисел из генератора добавляем в список
last = lst # Такое выражение тоже пустое т.к. результат генерации уже вызывался
print(new_list)
print(len(new_list))
print(*lst) # Пустой