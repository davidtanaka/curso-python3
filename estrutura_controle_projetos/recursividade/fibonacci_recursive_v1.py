# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade, sequencia=(0, 1)):
    # Condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))



if __name__ == '__main__':
    # Listar os 10 primeiros números da sequência
    for fib in fibonacci(10):
        print(fib)
