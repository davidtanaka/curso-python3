dicionario = {
    'nome': 'Caneta Chique',
    'preco': 16.89,
    'cor': 'Preta'
}

for chave in dicionario:
    print(chave)
print()

for valor in dicionario.values():
    print(valor)
print()

for chave, valor in dicionario.items():
    print(f'{chave} = {valor}')
print()

print(chave, valor)
