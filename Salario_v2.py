sal_hour = int(input('Salario por hora: '))
horas = float(input('Horas trabalhadas no mês: '))


def salario(horas):
    return sal_hour * horas


def IR():
    return Total * 0.11


def INSS():
    return IR() * 0.8


def Syndicate():
    return INSS() * 0.5


if __name__ == '__main__':
    Total = salario(horas)
    Salario_Bruto = Total
    Salario_Lq = Total - IR() - INSS() - Syndicate()
    print(f'Seu salario bruto é de R${Salario_Bruto}')
    print(f'Desconto de 11% (R${IR()}) pelo Imposto de Renda!')
    print(f'Desconto de 8% (R${INSS()}) pelo INSS!')
    print(f'Desconto de 5% (R${Syndicate()}) pelo Sindicato!')
    print(f'Seu salario liquido é de R${Salario_Lq}')
