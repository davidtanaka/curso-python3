a = '123'
b = ' de Oliveira 4'

print(a + b)  # Concatenação normal
print(a.__add__(b))  # Usando o método mágico __add__
print(str.__add__(a, b))  # Chamando diretamente da classe str

print(len(a))  # Obtendo o comprimento da string
print(a.__len__())  # Usando o método mágico __len__

print('1' in a)  # Verificando se '1' está na string
print(a.__contains__('1'))  # Usando o método mágico __contains__

print(dir(str))  # Listando os métodos disponíveis para strings
