# Calcular o peso ideal para uma pessoa
# a partir de sua altura usando a formula (72.7 * altura) - 58
def pesoid(alt):
    return float((72.7 * alt) - 58)


if __name__ == '__main__':
    alt = float(input('Insira a altura em metros: '))
    peso_ideal = pesoid(alt)
    print(f'Seu peso ideal é: {peso_ideal}Kg ')
