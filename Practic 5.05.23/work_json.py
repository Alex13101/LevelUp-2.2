import json

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

json_string = json.dumps(data, indent=4)
lst = json.loads(json_string)
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4) # indent - количество пробелов (для красоты вывода)

with open('test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)


# print(json_string)
# print(lst)