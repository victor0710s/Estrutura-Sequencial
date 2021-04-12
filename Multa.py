# Calcular a multa por excesso de peso.
# Limite = 50 quilos;
# 4 reais por quilo a mais

peso_peixe = float(input('Quantos quilos de peixe você está levando: '))
excesso = peso_peixe - 50.0


def multa(peso_peixe):
    return (excesso) * 4.0


if __name__ == '__main__':
    Pmax = multa(peso_peixe)
    if peso_peixe > 50.0:
        print(f'!Limite de peso excedido!Excesso de: {excesso}Kg')
        print(f'Valor da multa por execesso de peso: R$ {Pmax}')
    else:
        print('O peso informado está dentro dos limites.')

