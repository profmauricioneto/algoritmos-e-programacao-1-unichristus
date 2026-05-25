# criando a matriz inicialmente com valores zeros
matrix = []
for i in range(3):
    linha = [0]*4
    matrix.append(linha)
print(matrix)
# preenchendo a matriz com valores
for i in range(0, 3):
    for j in range(0, 4):
        matrix[i][j] = int(input(f'Digite o valor do elemento matrix[{i},{j}]: '))
print(matrix)