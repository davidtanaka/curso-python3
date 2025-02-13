from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    return(f'É necessário informar o raio,\n Sintaxe: {sys.argv[0]} <raio>')


def circulo():
    area_pi = pi
    if len(sys.argv) < 2:
        print(help())
        sys.exit(1)

    if not sys.argv[1].isnumeric():
        print(help())
        print(
            TerminalColor.ERRO + 
            'O raio deve ser um valor númerico'
            + TerminalColor.NORMAL
        )
        sys.exit(errno.EINVAL)
    else:
        raio = int(sys.argv[1])
        resultado = area_pi * raio ** 2
        return resultado


if __name__ =='__main__':
    print('A área do circulo é: ', circulo())
