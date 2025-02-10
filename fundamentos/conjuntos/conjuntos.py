a = {1, 2, 3}
print(type(a))  # Exibe o tipo do conjunto

# print(a[0])  # Isso daria erro, pois conjuntos não suportam indexação

a = set('coddddd3r')
print(a)  # Mostra os elementos únicos do conjunto

print('3' in a, 4 not in a)  # Verifica a presença de elementos

print({1, 2, 3} == {3, 2, 1, 3})  # Comparação de conjuntos (True, pois a ordem não importa)

# Operações com conjuntos
c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))  # União dos conjuntos

print(c1.intersection(c2))  # Interseção dos conjuntos

c1.update(c2)  # Atualiza c1 com os elementos de c2
print(c1)  # Mostra o novo c1

print(c2 <= c1)  # Verifica se c2 é subconjunto de c1

print(c1 >= c2)  # Verifica se c1 é um superconjunto de c2

print({1, 2, 3} - {2})  # Diferença entre conjuntos

print(c1 - c2)  # Diferença entre c1 e c2

c1 -= {2}  # Remove o elemento 2 de c1
print(c1)  # Exibe o novo c1
