
from random import randint
from src.main import get_number
# def foo(lst: list = []) -> int:
#     lst = lst.copy()
#     return  len(lst)

# lst = [1, 2, 3]
# lst = [[]*3]
# print(foo())
# print(lst)
# # lst2[0].append(1)
# # lst2[1].append(2)
# # lst2[2].append(3)

def get_data():

    json_data = None
    return json_data['status'] if json_data  and 'status' in json_data else 404
print(get_data())
print(get_number())
