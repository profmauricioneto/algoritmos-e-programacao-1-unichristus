vendas = [23, 42, 56, 64, 43, 24, 76, 55]
# calculo da média das vendas
acumulador = 0
for i in range(0, len(vendas)):
    acumulador += vendas[i]
media = acumulador/len(vendas)
print(int(media))

# meses que ultrapassaram a media
copia_vendas = vendas[:]
print(copia_vendas)
for i in range(0, len(vendas)):
    if (vendas[i] < int(media)):
        copia_vendas.remove(vendas[i])

print(f'Vendas ao longo dos meses: {vendas}')
print(f'Vendas acima da média: {copia_vendas}')