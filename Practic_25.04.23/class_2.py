# 1
numbers = []
for x in range(1, 100):
    if x % 3 == 0:
        numbers.append(x)

print(numbers)

# 2

even = []
for i in range(1, 100):
    if i % 2 == 0:
        even.append(i)

print(even)


# 3
divider = []
numb = int(input ("Введи целое число: "))

for c in range(1, numb):
    if numb % c == 0:
        divider.append(c)


print('Делители числа', numb,' ', divider)