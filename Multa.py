# Calcular a multa por excesso de peso.
# Limite = 50 quilos;
# 4 reais por quilo a mais

peso_peixe = float(input('Quantos quilos de peixe você está levando: '))


def multa(peso_peixe):
    return (peso_peixe - 50.0) * 4.0


if __name__ == '__main__':
    Pmax = multa(peso_peixe)
    if peso_peixe > 50.0:
        print(f'!Limite de peso excedido!n\
            Valor da multa por execesso de peso: R$ {Pmax}')
    else:
        print('O peso informado está dentro dos limites.')
