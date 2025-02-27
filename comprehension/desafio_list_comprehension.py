# O deafio consiste em dobrar o preço de todos os produtos

# Forma normal
# lista_precos = [500, 1500, 3000, 100, 25]
# lista_novos_precos = []
# for valor in lista_precos:
#     lista_novos_precos.append(valor * 2)
# print(lista_novos_precos)

# Com comprehension
lista_precos = [500, 1500, 3000, 100, 25]
lista_novos_precos = [i * 2 for i in lista_precos]
print(lista_novos_precos)
