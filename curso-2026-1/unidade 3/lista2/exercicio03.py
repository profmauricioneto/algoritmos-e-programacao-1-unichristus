salario = float(input("Salario: "))
prestacao_emprestimo = float(input("Prestacao do Emprestimo: "))

if (prestacao_emprestimo > 0.2*salario):
    print("Emprestimo concedido")
else:
    print("Emprestimo nao concedido")