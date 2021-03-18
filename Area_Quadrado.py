# O dobro da area de um quadrado

lado_square = input('Informe o lado do quadrado: ')
area = lado_square * 2
print('A area encontrada foi: ', area)


def help():
    print('O valor do lado nao pode ser negativo.')
    print('Sintaxe: {} <lado>'.format(lado_square))


def square(area):
    return float(area) * 2


if __name__ == '__main__':
    Area = square(area)
    for input in lado_square:
        if float(input) < 0 or float(input) == 0:
            help()

    else:
        print('O dobro da area do quadrado é: ', Area)
