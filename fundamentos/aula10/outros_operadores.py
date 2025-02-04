# Operadores de Membro
lista = [1, 2, 3, 'Ana', 'Claudia']
print(2 in lista)  # Verifica se o elemento 2 está na lista (retorna True)

# Operadores de Identidade
x = 4
y = x  # y recebe a mesma referência de x
z = 4  # Python pode reutilizar a mesma referência para pequenos inteiros
print(x is y)  # True, pois y é exatamente a mesma variável que x
print(y is z)  # True, pois z também pode compartilhar a mesma referência
print(x is not z)  # False, pois x e z são a mesma referência

lista1 = [9, 8, 4]
lista2 = lista  # lista2 recebe a mesma referência da lista original
lista3 = [9, 8, 4]  # Criada uma nova lista, mesmo conteúdo, mas referência diferente
print(lista1 is lista2)  # False, pois lista1 e lista2 são objetos diferentes
print(lista1 is lista3)  # False, pois lista1 e lista3 são listas distintas
print(lista1 is not lista3)  # True, pois lista1 e lista3 têm referências diferentes
