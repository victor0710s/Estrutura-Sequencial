# CONVERTER fahrenheit PARA CELSIUS

def Temperatura():
    return (f - 32) / 1.8


if __name__ == '__main__':
    f = int(input('Insira a Temp. em Fahrenheit: '))
    C = Temperatura()
    print(f'A conversão para Celsius deu: {C} C°')
