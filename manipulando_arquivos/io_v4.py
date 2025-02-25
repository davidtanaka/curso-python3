try:
    arquivo = open('pessoa.csv')

    for registro in arquivo:
        nome, idade = registro.strip().split(',')
        print(f'Nome: {nome}, Idade: {idade}')
except IndexError: ...

finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('O arquivo já foi fechado')
