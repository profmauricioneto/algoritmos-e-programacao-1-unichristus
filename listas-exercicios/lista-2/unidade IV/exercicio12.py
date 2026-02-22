distancia_percorrida = float(input("Entre com a distância percorrida (em km): "))
quantidade_gasolina = int(input("Quantidade de litros de gasolina: "))

consumo = distancia_percorrida / quantidade_gasolina

if (consumo <= 8):
    print("Venda o Carro!")
elif (consumo < 8 and consumo > 14):
    print("Econômico!")
else:
    print("Super econômico!")