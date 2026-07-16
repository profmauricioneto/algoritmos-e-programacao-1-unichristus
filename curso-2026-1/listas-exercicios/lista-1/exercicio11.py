comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
preco_por_metro = float(input("Preço por metro: "))

perimetro = 2 * (comprimento + largura)
custo = perimetro * preco_por_metro

print(f"O custo total é: {custo:.2f} reais")