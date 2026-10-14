print('SIMULADOR DE PARCELAS')
emprestimo = float(input('Emprestimo Desejado: '))

while(True):
    parcelas = int(input('Quantidade de parcelas [1 a 12]: '))

    if (parcelas >= 1 and parcelas <= 12):
        break
    else:
        print('Parcela Inválida!')

juros = 0
if (parcelas >= 1 and parcelas <= 2):
    juros = emprestimo*0.02
elif (parcelas >= 3 and parcelas < 6):
    juros = emprestimo*0.1
elif (parcelas >= 6 and parcelas < 9):
    juros = emprestimo*0.15
elif (parcelas >= 9 and parcelas < 12):
    juros = emprestimo*0.2
else:
    juros = emprestimo*0.25 

total = emprestimo + juros
valor_parcela = total/parcelas

print(f'Total = R${total: .2f} | Juros = R${juros: .2f} | Parcelas = {parcelas} | Valor/Parcela = R${valor_parcela: .2f}')