from string import Template

nome, idade = 'Ana', 30

# Formatações de string em diferentes versões do Python
print('Nome: %s Idade: %d' % (nome, idade))  # Mais antiga (Python 2 e primeiras versões do 3)
print('Nome: {0} Idade: {1}'.format(nome, idade))  # Python < 3.6
print(f'Nome: {nome} Idade: {idade}')  # Python >= 3.6

# Usando Template para substituição
s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))  # Substituição com Template
