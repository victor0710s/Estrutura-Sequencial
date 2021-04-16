# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de
# a serem compradas e o preço total
import math

Area_parede = int(input('Qual a area da parede a ser pintada?:'))
L1 = float(Area_parede / 3)
if L1 <= 18:
    print('1 lata de tinta custa de 18L custa R$ 80,00.')
else:
    x = math.ceil(L1 / 18)
    Platas = x * 80
    print(f'Precisará de {x}, e valor total é de R${Platas}.')
