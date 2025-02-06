# Definição de uma "tupla errada"
tupla_errada = ('Um')  # Isso NÃO cria uma tupla, pois parênteses sozinhos não definem tuplas em Python.

# Definição correta de uma tupla
tupla = ('Um',)  # A vírgula indica que é uma tupla de um único elemento.

# Verificando o tipo de cada variável
print(type(tupla_errada))  # Isso retornará <class 'str'>, pois 'tupla_errada' é apenas uma string.
print(type(tupla))  # Isso retornará <class 'tuple'>, pois a vírgula define como tupla.

# Acessando um elemento da tupla
print(tupla[0])  # Retorna 'Um', pois é o único elemento.

# Definição de uma tupla com várias cores
cores = ('Verde', 'Amarelo', 'Vermelho', 'Azul')

# Acessando elementos da tupla usando índices positivos e negativos
print(cores[-1])  # Retorna 'Azul', pois índices negativos contam de trás para frente.
print(cores[2])  # Retorna 'Vermelho', pois é o terceiro elemento (índices começam do 0).

# Métodos úteis de tuplas
print(cores.index('Vermelho'))  # Retorna 2, que é o índice do elemento 'Vermelho'.
print(cores.count('Vermelho'))  # Retorna 1, pois 'Vermelho' aparece uma vez na tupla.
print(len(cores))  # Retorna 4, que é o número total de elementos na tupla.
