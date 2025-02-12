from math import pi
import sys


def circulo():
    area_pi = pi
    if len(sys.argv) < 2:
        print(f'É necessário informar o raio,\n Sintaxe: {sys.argv[0]} <raio>')
    else:
        raio = int(sys.argv[1])
        resultado = area_pi * raio ** 2
        return resultado


if __name__ =='__main__':
    print('A área do circulo igual é: ', circulo())
