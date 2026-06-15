quantidade_alunos = int(input('Digite a quantidade de alunos: '))
# inicialização do array com 0
notas = []
for i in range(quantidade_alunos):
    linha = [0] * 3
    notas.append(linha)
print(notas)

# preencher a matriz de notas dos alunos
for i in range(quantidade_alunos):
    print(f'Notas do aluno {i}')
    for j in range(3):
        notas[i][j] = float(input(f'Nota[{i}][{j}]: '))
print(f"Matriz de Notas dos Alunos: {notas}")
        
# percorrer a matriz e calcular a média
medias = []
for i in range(quantidade_alunos):
    media = 0
    for j in range(3):
        media = media + notas[i][j]
    media = media/3
    medias.append(media)
print(f"Medias = {medias}")

# calculo da média das médias dos alunos e
# verificar qual é a maior média da turma
# e quem é o aluno.
media_turma = 0
for i in range(len(medias)):
    media_turma += medias[i]
media_turma = media_turma/len(medias)
print(f'Media da turma: {media_turma: .2f}')

maior_media = medias[0]
indice_maior_media = 0
for i in range(len(medias)):
    if (maior_media < medias[i]):
        maior_media = medias[i]
        indice_maior_media = i

print(f'Maior média da turma: {maior_media}')
print(f'Aluno de maior média = {indice_maior_media}')