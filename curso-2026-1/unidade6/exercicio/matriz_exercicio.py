# inicialização da matriz
# matriz = [[0, 0], [0, 0]]
matriz = []
resultante = []
for i in range(0, 2):
    linha = [0]*2
    matriz.append(linha)
    resultante.append(linha)
# preenchendo a matriz com os valores fornecidos pelo usuario 
for i in range(0, 2):
    for j in range(0, 2):
        matriz[i][j] = float(input(f'matriz[{i}][{j}] = '))

# percorrendo a matriz e verificando quem é o maior valor!
maior = matriz[0][0]
for i in range(0, 2):
    for j in range(0, 2):
        if (maior < matriz[i][j]):
            maior = matriz[i][j]
print(matriz)
print(f'O maior valor da matriz é {maior}')

# resultante = [[0, 0], [0, 0]]
for i in range(0, 2):
    for j in range(0, 2):
        resultante[i][j] = matriz[i][j] * maior
        
print(resultante)