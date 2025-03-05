def executa(funcao):
    if callable(funcao):
        return funcao()
    print('Isso não é uma função válida!')


def bom_dia():
    return 'Bom dia'


def boa_tarde():
    return 'Bom dia'


if __name__ == '__main__':
    print(executa(bom_dia))
    print(executa(boa_tarde))
