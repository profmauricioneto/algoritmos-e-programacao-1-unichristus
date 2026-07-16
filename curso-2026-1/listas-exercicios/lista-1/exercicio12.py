consumo_mensal = float(input("Qual o consumo mensal de água (m3): "))
consumo_total = 0

if (consumo_mensal <= 10):
    consumo_total = 30
elif (consumo_mensal > 10 and consumo_mensal <= 20):
    consumo_excedente = consumo_mensal - 10
    consumo_total = 30 + (consumo_excedente * 3)
else:
    consumo_excedente = consumo_mensal - 20
    consumo_total = 2 * 30 + (consumo_excedente * 5)
    
print(f"Consumo registrado: {consumo_mensal} m3")
print(f"Valor total da conta: {consumo_total: .2f} m3") 
