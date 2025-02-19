# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# def fibonacci(limite):
#     resultado = [0, 1]
#     print(f'{resultado[-2]}, {resultado[-1]}', end=',')
#     while resultado[-1] < limite:
#         proximo_numero = resultado[-2] + resultado[-1]
#         if proximo_numero >= limite:
#             break
#         resultado.append(proximo_numero)
#         print(proximo_numero, end=',')
 
# if __name__ == '__main__':
#     fibonacci(2000)


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(2000):
        print(fib)
