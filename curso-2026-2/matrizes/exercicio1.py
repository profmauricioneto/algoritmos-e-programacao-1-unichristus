valor_indices = int(input('Qual os valor dos indices: '))

# criar a matriz
mat = []
for i in range(valor_indices):
    linha = [0] * valor_indices
    mat.append(linha)

total = 0
# preencher a matriz
for i in range(valor_indices):
    for j in range(valor_indices):
        mat[i][j] = int(input(f'mat[{i}][{j}]: '))
        if (i == j):
            total = total + mat[i][j]
        
print(mat)
print(f'Soma dos elementos da diagonal principal = {total}')