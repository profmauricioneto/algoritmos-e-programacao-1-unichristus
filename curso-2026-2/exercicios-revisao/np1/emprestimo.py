salario = float(input('Digite o seu salario: '))
prestacao = float(input('Digite a prestação do empréstimo: '))
if (prestacao > 0.2*salario):
    print('Emprestimo não concedido.')
else:
    print('Emprestimo concedido.')