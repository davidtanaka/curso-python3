def gerar_tabuadas():
    numero_usuario = int(input('Digíte um número ínteiro: '))
    print('Essa é a tabuada do seu número;')
    for numero in range(1, 11):
        print(f'{numero_usuario} X {numero} = {numero * numero_usuario}')
    continuar = input('você deseja continuar? [S/N]')
    if continuar.lower() == 's':
        gerar_tabuadas()
    else:
        print('Adeus')

if __name__ == '__main__':
    gerar_tabuadas()
