salario = float(input("Valor do salario: "))
prestacao = float(input("Valor do emprestimo: "))

if prestacao > 0.2*salario:
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido!")