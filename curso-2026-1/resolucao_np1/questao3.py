distancia = float(input("Distancia (km): "))
combustivel = float(input("Quantidade de combustível (l): "))
preco_litro = float(input("Valor do litro de combustível (R$): "))

consumo_medio = distancia / combustivel
print(f"Valor do consumo médio: {consumo_medio: .2f}")
custo_total_combustivel = combustivel * preco_litro
print(f"Custo total do combustível na viagem: {custo_total_combustivel: .2f}")