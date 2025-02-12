from math import pi


def circulo():
    area_pi = pi
    raio = float(input('Informe o raio: '))
    resultado = area_pi * raio ** 2
    return resultado


if __name__ =='__main__':
    print('A área do circulo igual é: ', circulo())
