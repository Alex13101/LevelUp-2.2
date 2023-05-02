def foo(a=1, b=2, c=3):
    return a + b + c


def get_number(foo, **kwargs):
    print(foo(**kwargs))
    return 42


print(get_number(foo, a=1, b=2, c=3))


# print(get_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(get_number(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10))


def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "returned", result)
        return result

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def mul(x, y):
    return x * y


@logger
def sub(x, y):
    return x - y


mul(2, 3)

add(2, 3)

sub(9, 6)
