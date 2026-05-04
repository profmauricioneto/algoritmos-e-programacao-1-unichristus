quantidade_notas = int(input('Digite a quantidade de notas: '))

notas = [0.0]*quantidade_notas
media = 0
for i in range(0, quantidade_notas):
    notas[i] = float(input(f'Digite a nota[{i}]: '))
    media = media + notas[i]

media = media / quantidade_notas
print(f'Media da turma: {media: .1f}')

for i in range(0, quantidade_notas):
    if (notas[i] >= 4 and notas[i] < 7):
        print(f'Aluno do indice {i} esta de AF com nota = {notas[i]}')
    
# Modifique o programa (notas_lista.py) tal que depois de receber as notas dos alunos, calcular a média da turma, e mostrar a posição na lista e a nota dos alunos que ficaram de AF (4 <= nota < 7).