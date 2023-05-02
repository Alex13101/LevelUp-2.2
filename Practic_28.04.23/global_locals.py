from random import *

global_var =20

def func():
    a = 10
    #local_var = 20
    print(locals())
    print(global_var)


func()
print(globals())