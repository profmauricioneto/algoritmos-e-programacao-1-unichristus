distancia = float(input('Digite a distância em km: '))
gasolina = float(input('Digite a gasolina consumida em litros: '))
consumo = distancia / gasolina
print(f'Consumo: {consumo: .2f}')
if (consumo < 8):
    print('Venda o Carro pelo Amor de Deus!')
elif (consumo >= 8 and consumo <= 12):
    print('Econômico.')
else:
    print('Super Econômico.')