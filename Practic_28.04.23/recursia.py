

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) #Умножает число на число -1 и вызывается снова
                                  # функция. До тех пор пока n не будет равно 0


print(factorial(5))