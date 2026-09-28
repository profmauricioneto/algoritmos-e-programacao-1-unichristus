custo_total = float(input('Custo total da Viagem: '))
saldo_inicial = float(input('Saldo Inicial: '))
deposito_mensal = float(input('Deposito Mensal: '))

rendimento_poupanca = 0.5
valor_atual = saldo_inicial
meses = 1

while(custo_total >= valor_atual):
    valor_atual += deposito_mensal
    valor_atual = valor_atual*(1 + rendimento_poupanca/100)
    print(f'Valor atual R$:{valor_atual: .2f} - Mês: {meses}')
    meses += 1

print(f'Demorou {meses-1} meses para atingir o valor da viagem!')