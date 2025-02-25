arquivo = open('pessoa.csv')
for registro in arquivo:
    nome, idade = registro.strip().split(',')
    print(f'Nome: {nome}, Idade: {idade}')
arquivo.close()
