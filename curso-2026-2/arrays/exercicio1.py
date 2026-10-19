notas = [0] * 10
cont_aprovados = 0

for i in range(len(notas)):
    notas[i] = float(input('Digite sua nota: '))
    
    if (notas[i] < 4):
        print(f'Aluno {i + 1} - REPROVADO')
    elif (notas[i] >= 7):
        print(f'Aluno {i + 1} - APROVADO')
        cont_aprovados += 1
    else:
        print(f'Aluno {i + 1} - AF (AVALIACAO FINAL)')

print(f'Quantidade de Aprovados: {cont_aprovados}')
print('FIM DE PROGRAMA')