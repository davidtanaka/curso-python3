# String
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print('fim\n')


# Listas
aprovados = ['Joana', 'Ket', 'Davi', 'João']
for nome in aprovados:
    print(nome)
print()

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)
print()


# Tuplas
dias_semana = (
    'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta',
    'Sexta', 'Sabado', 'Domingo'
)
for dia in dias_semana:
    print(f'Hoje é {dia}')
print()

# Set
for letra in set('Muito legal'):
    print(letra)
print()   

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
