# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        if len(resultado) == quantidade:
            break
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # Listar os 10 primeiros números da sequência
    print(fibonacci(10))
