preco_antigo = float(input("Digite o valor antigo: "))
preco_novo = 0

if (preco_antigo <= 50.0):
    preco_novo = preco_antigo + 0.05*preco_antigo
elif (preco_antigo > 50 and preco_antigo <= 100):
    preco_novo = preco_antigo + 0.1*preco_antigo
else:
    preco_novo = preco_antigo + 0.15*preco_antigo
    
print(f"O preço atual com reajuste é: {preco_novo: .2f}")