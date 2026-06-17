qtd_cidades = int(input('Digite a quantidade de cidades: '))

# criando a matriz
registros = []
for i in range(qtd_cidades):
    linha = [0]*7
    registros.append(linha)
print(registros)

# preenchendo a matriz
for i in range(qtd_cidades):
    print(f'Cidade {i}')
    for j in range(7):
        registros[i][j] = float(input(f'Temperatura [{i}][{j}]: '))
print(registros)

# percorrendo a matriz e calculando as médias
medias = []
for i in range(qtd_cidades):
    media = 0
    for j in range(7):
        media = media + registros[i][j]
    media = media/7
    medias.append(media)
print(f'Medias das cidades: {medias}')

# procurar quem é a maior média
maior_media = medias[0]
indice_maior_media = 0
for i in range(len(medias)):
    if (maior_media < medias[i]):
        maior_media = medias[i]
        indice_maior_media = i
print(f'Maior média = {maior_media}')
print(f'A maior média é da cidade {indice_maior_media}')

# procurando o maior registro de temperatura
maior_registro = registros[0][0]
for i in range(qtd_cidades):
    for j in range(7):
        if maior_registro < registros[i][j]:
            maior_registro = registros[i][j]
print(f'Maior valor de temperatura registro foi {maior_registro}')

