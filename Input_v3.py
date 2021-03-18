# O total do trimestre é 30 pontos e a media é 15

# NOTAS
B1 = float(input('Informe sua nota no 1ºBimestre: '))
B2 = float(input('Informe sua nota no 2ºBimestre: '))
B3 = float(input('Informe sua nota no 3ºBimestre: '))
B4 = float(input('Informe sua nota no 4ºBimestre: '))
Total = B1 + B2 + B3 + B4
Media = Total / 4


if __name__ == '__main__':
    print('A média das suas notas é: ', Media)
    if Total < 60:
        print('Você reprovou!!')

    else:
        print('Parabéns, você passou de ano!!')
