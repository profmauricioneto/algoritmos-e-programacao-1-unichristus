# criando a matriz de zeros
mat = []
for i in range(2):
    linha = [0] * 2
    mat.append(linha)
    
# preencher a matriz!
for i in range(2):
    for j in range(2):
        mat[i][j] = int(input(f'mat[{i}][{j}] = '))
        
maior = mat[0][0]
# percorrer a matriz analisando se existe algum numero maior
# que a referencia
for i in range(2):
    for j in range(2):
        if (maior < mat[i][j]):
            maior = mat[i][j]
            
print(f'O maior valor da matriz = {maior}')
print(f'Matriz de entrada: {mat}')

mat_r = []
for i in range(2):
    linha = [0]*2
    for j in range(2):
        linha[j] = mat[i][j] * maior
    mat_r.append(linha)
print(f'Matriz com fator multiplicativo = {mat_r}')