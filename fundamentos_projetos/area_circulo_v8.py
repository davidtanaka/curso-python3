from math import pi


def circulo():
    area_pi = pi
    raio = float(input('Informe o raio: '))
    resultado = area_pi * raio ** 2
    print(f'Área do círculo é igual à: {resultado:.2f}')


if __name__ =='__main__':
    circulo()
