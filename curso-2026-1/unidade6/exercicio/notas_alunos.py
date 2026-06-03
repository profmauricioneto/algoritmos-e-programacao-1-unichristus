# criação do matriz com valores 0
relatorio = []
for i in range(2):
    linha = [0]*3
    relatorio.append(linha)
print(relatorio)

# preenchendo as notas dos alunos
for i in range(0, 2):
    print(f'Entre com as notas do aluno {i}')
    for j in range(0, 3):
        relatorio[i][j] = float(input(f'Nota[{i},{j}] = '))
print(relatorio)

# verificar e mostrar o menor valor de nota de cada aluno
np1 = 0
np2 = 0
np3 = 0
for i in range(0, 2):
    menor_nota = relatorio[i][0]
    indice_menor_nota = 0
    for j in range(0, 3):
        if (menor_nota < relatorio[i][j]):
            menor_nota = relatorio[i][j]
            indice_menor_nota = j
    if (indice_menor_nota == 0):
        np1 += 1
    if (indice_menor_nota == 1):
        np2 += 1
    if (indice_menor_nota == 2):
        np3 += 1

print(f"Quantidade de NP1 baixa: {np1}")
print(f"Quantidade de NP2 baixa: {np2}")
print(f"Quantidade de NP3 baixa: {np3}")
            