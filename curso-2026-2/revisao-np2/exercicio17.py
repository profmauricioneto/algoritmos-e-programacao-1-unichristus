deposito_mensal = float(input('Deposito Mensal R$: '))
rendimento_mensal = float(input('Rendimento mensal %:'))
meta = float(input('Meta R$: '))

total_depositado = 0
saldo_acumulado = deposito_mensal
meses = 0
total_rendimento = 0
while(saldo_acumulado < meta):
    total_depositado += deposito_mensal
    total_rendimento += saldo_acumulado*(rendimento_mensal/100)
    saldo_acumulado = saldo_acumulado+ saldo_acumulado*(rendimento_mensal/100) + deposito_mensal
    print(f'Mês {meses} - Saldo Acumulado: {saldo_acumulado: .2f}')
    meses += 1
print(f'Meta atingida em: {meses} meses')
print(f'Saldo Final = R${saldo_acumulado: .2f}')
print(f'Total depositado = R${total_depositado: .2f} | Rendimento: R${total_rendimento: .2f}')
