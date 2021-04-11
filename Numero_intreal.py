# 1. Pedir 2 números inteiros e  um número real:
# a -> o produto do dobro do primeiro com metade do segundo
# b -> a soma do triplo do primeiro com o terceiro.
# c -> o terceiro elevado ao cubo.

def numINT(num1):
    return (num1 * 2) * (num2 / 2)


def numIR(num2):
    return (num1 * 3) + num3


def num(num3):
    return num3 ** 3


if __name__ == '__main__':
    num1 = int(input('Insira o número inteiro 1: '))
    num2 = int(input('Insira o número inteiro 2: '))
    num3 = float(input('Insira o número 3: '))
    letra_a = numINT(num1)
    letra_b = numIR(num2)
    letra_c = num(num3)

print('Resolução letra "A": ', letra_a)
print('Resolução letra "B": ', letra_b)
print('Resolução letra "C": ', letra_c)
