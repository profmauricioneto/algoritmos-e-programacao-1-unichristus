# criar a matriz
mat = []
for i in range(5):
    linha = [0] * 3
    mat.append(linha)
print(mat)

# preencher a matriz com as notas de cada aluno
for i in range(5):
    for j in range(3):
        mat[i][j] = float(input(f'Nota [{j+1}] do aluno[{i+1}]: '))