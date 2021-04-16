#! python
# Bibliotecas Importadas
import math
import colorama
colorama.init()

Norm = '\033[0m'
A = '\033[36m'
Op = '\033[1;93m'
N = '\033[31m'
P = '\033[32m'
name = '\033[34m'

# Funções


def options(Decisão):
    print(N + """
    Digite (1) se deseja comprar somente latas de tinta;
    Digite (2) se deseja comprar somente galões de tinta;
    Digite (3) se deseja comprar ambos;""" + Norm)
    Decisão = eval(input('Qual opção você deseja:'))
    while not 1 <= Decisão <= 3:
        Decisão = int(input('Digite a opção escolhida:'))
    if Decisão == 1:
        print()
        print(P + 'Você precisará de %dL de tinta;\n\
              %d latas e irá pagar R$%d!' + Norm % (Litros, QTDL, PLata))
    elif Decisão == 2:
        print()
        print(P + 'Você precisará de %dL de tinta;\n\
               %d galões e irá pagar R$%d!' % (Litros, QTDG, PGalão) + Norm)
    elif Decisão == 3:
        a1 = int(Ltfolga/18)
        a2 = Ltfolga % 18
        a3 = math.ceil(a2/3.6)
        a4 = ((a1*80)+(a3*25))
        print(P + f'Você precisará de {Litros}L de tinta;\n\
        {a1} latas e {a3} galões e irá pagar R${a4}!' + Norm)
    else:
        return Decisão
    print()


def Menu(a):
    print(Op + 'Suas opçoes:' + Norm)
    print('')
    print(Op + '1º) Calcular área.' + Norm)
    print(Op + '2º) Mostrar preço dos produtos.' + Norm)
    print(Op + '3º) Calcular preço pela área a ser pintada.' + Norm)
    print(Op + '4º) Sair do programa.' + Norm)
    print('')
    opção = int(input('Escolha a opção desejada:'))
    while not 1 <= opção <= 4:
        print()
        opção = int(input('Escolha uma opção de 1 à 4:'))
    else:
        return opção


def price(a):
    print()
    print(A + 'Temos latas de tinta contendo 18L e no valor de R$80,00!'
          + Norm)
    print(A + 'E também galões de tinta contendo 3,6L e no valor de R$25,00!'
          + Norm)
    print()


# Resolução
print('----------------')
print(name + '!Bem-vindo a Casa de Tintas Aquarela!' + Norm)
loop = 1
Area = 0
choice = 0

while loop:
    choice = Menu(1)

    if choice == 1:
        Area = eval(
            input('Qual a area em metros quadrados (m²) a ser pintada?:'))
        Litros = float(Area / 6)
        Ltfolga = math.ceil(Litros * 1.1)
        QTDL = math.ceil(Ltfolga / 18)
        QTDG = math.ceil(Ltfolga / 3.6)
        PLata = QTDL * 80
        PGalão = QTDG * 25
    elif choice == 2:
        price(1)
    elif choice == 3:
        if Area == 0:
            print()
            print('Execute a primeira opção [Calcula área]!')
            print()
        else:
            options(1)
    elif choice == 4:
        loop = 0

print()
print(name + '!OBRIGRADO PELA SUA PREFERÊNCIA!' + Norm)
print('-----------------')
