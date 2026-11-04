temperatura = [0]*7
dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

media = 0
for i in range(len(temperatura)):
    temperatura[i] = float(input(f'Temperatura [{i + 1}]: '))
    media = media + temperatura[i]

media = media/len(temperatura)
maior_temp = temperatura[0]
menor_temp = temperatura[0]

qtd_acima_media = 0
for i in range(len(temperatura)):
    if (temperatura[i] > maior_temp):
        maior_temp = temperatura[i]
    if (temperatura[i] < menor_temp):
        menor_temp = temperatura[i]
    if (temperatura[i] > media):
        qtd_acima_media += 1
    
print(f'Maior Temperatura: {maior_temp}')
print(f'Menor Temperatura: {menor_temp}')
print(f'Media: {media: .2f}')     
print(f'Quantidade de dias Acima da Média: {qtd_acima_media}')