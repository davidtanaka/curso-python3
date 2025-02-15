# while True:
#     print('Isso é infinito')

from random import randint

numerado_informado = 0
numero_secreto = randint(0, 9)

while numerado_informado != numero_secreto:
    print('Tente acertar o número que estou pensando')
    numerado_informado = int(input('Digite um número: '))

print(f'você acertou o número secreto => {numero_secreto}')
