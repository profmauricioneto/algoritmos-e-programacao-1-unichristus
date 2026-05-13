def calcular_consumo_mensal(kwh):
    total_conta = 0
    if (kwh <= 100):
        total_conta = kwh * 0.5
        return total_conta
    else:
        excedente = kwh - 100
        total_conta = (100 * 0.5) + (excedente*0.75)
        return total_conta

def main():
    total_pago_anual = 0
    for i in range(1, 13):
        consumo = float(input(f'Digite o consumo do mês {i}: '))
        conta = calcular_consumo_mensal(consumo)
        print(f'Valor a ser pago no mês {i} = {conta}')
        total_pago_anual = total_pago_anual + conta
    print(f'Total pago no ano: {total_pago_anual}')
        
main()