quantidade_notas = int(input('Digite a quantidade de Notas: '))
notas = [0.0] * quantidade_notas
media = 0

# preenchendo o array
for i in range(quantidade_notas):
    notas[i] = float(input(f'Digite a {i+1}th nota: '))
    media = media + notas[i]
# calculo da média
media = media/quantidade_notas
print('Média da turma = ', media)

# apresentar os dados do array 
for i in range(quantidade_notas):
    if notas[i] >= media:
        print(f'A nota{i} = ', notas[i])