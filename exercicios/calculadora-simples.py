def calculadora():
    x = float(input('digite um número: '))
    y = float(input('digite outro número: '))
    tipo = input('Digite a operação desejada [+ para soma, - para subtração, x para multiplicação, / para divisão]: ')
    if tipo == 'x':
        return x * y
    elif tipo == '+':
        return x + y
    elif tipo == '-':
        return x - y
    elif tipo == '/':
        return x / y
    else:
        print('Digite um arguumento válido')

if __name__ == '__main__':
    print(calculadora())
