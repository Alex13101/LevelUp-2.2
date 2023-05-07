import csv

with open('test.csv', 'r', encoding= 'utf-8') as f:
    data = f.read().strip().split('\n')[1:]
    result =[]


    print(*data, sep='\n')
    for line in data:
        result.append(line.split(';'))
    print(result)

with open('test2.csv', 'w', encoding = 'utf-8') as f:
    for line in result:
        f.write(';'.join(line) + '\n')

