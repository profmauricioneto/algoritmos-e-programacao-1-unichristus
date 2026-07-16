temperaturas = []
somatorio_temp = 0
for i in range(0, 10):
    temp = float(input("Digite a temperatura: "))
    temperaturas.append(temp)
    if i == 0:
        maior_valor = temp
        menor_valor = temp
    else:
        if maior_valor < temp:
            maior_valor = temp
        if menor_valor > temp:
            menor_valor = temp
    somatorio_temp += temp
    
media = somatorio_temp/len(temperaturas)
print(f"A média das temperaturas: {media: .2f}")
print(f"Maior temperatura: {maior_valor: .2f}")
print(f"Menor temperatura: {menor_valor: .2f}")
    