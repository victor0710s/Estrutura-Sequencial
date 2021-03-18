# 1.TEM QUE PEDIR O RAIO DO CIRCULO E DEVOLVER A AREA
from math import pi
import sys
import errno
import colorama
colorama.init()

Resp = '\033[1;32m'
Warn = '\033[1;33m'
Erro = '\033[91m'
Norm = '\033[0m'


def help():
    print(Warn + 'É necessário informar o raio do circulo!!' + Norm)
    print('Sintaxe: {} <raio>'.format(sys.argv[0]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(Erro + 'O raio deve ser um valor numérico!!' + Erro)
        sys.exit(errno.EINVAL)

raio = sys.argv[1]
area = circulo(raio)
print(Resp + 'A area do circulo é: ' + Norm, area)
