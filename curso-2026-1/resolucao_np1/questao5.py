consumo = float(input('Valor do consumo: '))
desconto = 0

if (consumo >= 25):
    desconto = consumo*0.1
    print(f"Direito ao desconto de 10% = {desconto: .2f}")
else:
    print("Sem desconto.")

valor_a_pagar = consumo - desconto
print(f"Valor final a pagar: {valor_a_pagar: .2f}")