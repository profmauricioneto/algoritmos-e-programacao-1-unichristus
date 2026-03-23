preco_antigo = float(input("Digite o preco antigo: "))
preco_atualizado = 0

if (preco_antigo <= 50):
    preco_atualizado = preco_antigo*1.05
elif (preco_antigo > 50) and (preco_antigo <= 100):
    preco_atualizado = preco_antigo*1.1
else:
    preco_atualizado = preco_antigo*1.15

print(f"Valor do Preço Atualizado: {preco_atualizado: .2f}")