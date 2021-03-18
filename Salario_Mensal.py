#! python
# Pedir e calcular o ganho por horas

def salario(horas):
    return sal_hour * horas


if __name__ == '__main__':
    sal_hour = int(input('Salario por hora: '))
    horas = float(input('Horas trabalhadas no mês: '))
    Total = salario(horas)
    print(f'Seu salario nesse mês foi é de: R${Total}')
