with open('pessoa.csv') as arquivo:
    for pessoa in arquivo:
        nome, idade = pessoa.strip().split(',')
        print(f'Nome: {nome}, Idade: {idade}')
        
if arquivo.closed: 
    print('Arquivo Fechado!!')
