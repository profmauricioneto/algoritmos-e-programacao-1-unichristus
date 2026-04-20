def calculo_valor_conta(consumo_mensal):
    if (consumo_mensal <= 100):
        return consumo_mensal*0.5
    else:
        kwh_diferenca = consumo_mensal - 100
        return ((100 * 0.5) + (kwh_diferenca * 0.75))
    
def main():
    kwh_mensal = float(input('Digite a quantidade de KWh consumido no mês: '))
    
    conta = calculo_valor_conta(kwh_mensal)
    
    print(f'Valor a ser pago será R$: {conta}') 
    
main()