# alunos = ["huguinho", "zezinho", "luiziho", "astolfo", "gezebel"]
# notas = [5, 8, 2.5, 10, 7]
import matplotlib.pyplot as plt
alunos = ['']*5
notas = [0]*5

for i in range(len(alunos)):
    alunos[i] = input('Nome Aluno: ')
    notas[i] = float(input('Nota: '))

media_turma = 0
cont_aprovado = 0
cont_reprovado = 0
cont_recuperacao = 0
# faixas
cont_faixa_1 = 0 # 0 - 4
cont_faixa_2 = 0 # 4 - 6
cont_faixa_3 = 0 # 6 - 8
cont_faixa_4 = 0 # 8 - 10

for i in range(len(notas)):
    media_turma += notas[i]
    
    if(notas[i] >= 6.0):
        cont_aprovado += 1
        print(f'Aluno: {alunos[i]} - APROVADO')
    elif (notas[i] < 4.0):
        cont_reprovado += 1
        print(f'Aluno: {alunos[i]} - REPROVADO')
    else:
        cont_recuperacao += 1
        print(f'Aluno: {alunos[i]} - RECUPERACAO')
        
        
    if (notas[i] <= 4.0):
        cont_faixa_1 += 1
    elif(notas[i] <= 6.0):
        cont_faixa_2 += 1
    elif (notas[i] <= 8.0):
        cont_faixa_3 += 1
    else:
        cont_faixa_4 += 1

media_turma = media_turma/len(notas)
print(f'Média da turma = {media_turma: .1f}')
print(f'aprovados: {cont_aprovado} | reprovados: {cont_reprovado} | recuperacao: {cont_recuperacao}')

print('------- HISTOGRAMA -----------')
print('0-4 | ' + '*'*cont_faixa_1 )
print('4-6 | ' + '*'*cont_faixa_2)
print('6-8 | ' + '*'*cont_faixa_3)
print('8-10 | ' + '*'*cont_faixa_4)

plt.hist(notas)
plt.xlabel('faixas')
plt.ylabel('Notas')
plt.title('Notas por Faixa de Valores')
plt.show()
