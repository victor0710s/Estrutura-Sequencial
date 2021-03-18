# CONVERTER fahrenheit PARA CELSIUS


def Temperatura():
    return round(C / 1.8 + 32)


if __name__ == '__main__':
    C = float(input('Insira a Temp. em graus Celsius: '))
    f = Temperatura()
    print(f'A conversão para Fahrenheit deu aprox.: {f} °F')
