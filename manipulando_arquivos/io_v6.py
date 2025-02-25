with open('pessoa.csv', 'r') as arquivo:
    with open('pessoas.txt', 'w') as saida:

        for pessoa in arquivo:
            nome, idade = pessoa.strip().split(',')
            print(f'Nome: {nome}, Idade: {idade}', file=saida)
        
if arquivo.closed: 
    print('Arquivo Fechado!!')

if saida.closed: 
    print('Arquivo de saída Fechado!!')
