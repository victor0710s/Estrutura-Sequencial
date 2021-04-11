# Calcular o peso ideal para uma pessoa
# a partir de sua altura e sexo usando a formula:
# Homens > (72.7 * altura) - 58 ///// Mulheres >  (62.1 * altura) - 44.7

sexo = int(input('Digite seu sexo: (1)Para homem (2)Para mulher: '))

if sexo == 1:
    aH = float(input('Digite sua altura: '))
    vH = 72.7 * aH
    rH = vH - 58
    print('Seu peso ideal é ', rH, 'quilos')
elif sexo == 2:
    aM = float(input('Digite sua altura: '))
    vM = 62.1 * aM
    rM = vM - 44.7
    print('Seu peso ideal é ', rM, 'quilos')
