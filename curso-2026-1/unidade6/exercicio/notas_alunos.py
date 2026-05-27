# criação do matriz com valores 0
relatorio = []
for i in range(5):
    linha = [0]*3
    relatorio.append(linha)
print(relatorio)
# preenchendo as notas dos alunos
for i in range(0, 5):
    print(f'Entre com as notas do aluno {i}')
    for j in range(0, 3):
        relatorio[i][j] = float(input(f'Nota[{i},{j}] = '))
print(relatorio)

# verificar e mostrar o menor valor de nota de cada aluno