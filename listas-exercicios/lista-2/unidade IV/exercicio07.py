valor_produto = float(input("Digite o valor do produto: "))
estado = input("Digite a sigla do estado de destino do produto: ").lower()
custo_final = 0

if estado == "mg":
    custo_final = valor_produto + 0.07*valor_produto
elif estado == "sp":
    custo_final = valor_produto + 0.12*valor_produto
elif estado == "rj":
    custo_final = valor_produto + 0.15*valor_produto
elif estado == "ms":
    custo_final = valor_produto + 0.08*valor_produto
else:
    custo_final = valor_produto
    
print(f"Custo final do produto: {custo_final: .2f}")