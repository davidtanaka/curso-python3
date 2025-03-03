def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c

def soma_ilimitada(*numeros):
    return sum(numeros)

if __name__ == '__main__':
    print(soma_2(3, 4))

    print(soma_3(1, 6, 2))
    
    print(soma_ilimitada(1, 54, 2, 5, 7, 1, 7, 4))

    nums = (1, 2, 3)
    print(soma_3(*nums))
