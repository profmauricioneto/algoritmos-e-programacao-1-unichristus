valor_emprestimo = float(input("Valor do empréstimo: "))
taxa_juros_mensal = float(input("Taxa de juros mensal(%): "))
qtd_meses = int(input("Quantidade de meses: "))
total_juros = 0
total = 0

for i in range(0, qtd_meses):
    total_juros += valor_emprestimo*(taxa_juros_mensal/100)

total = valor_emprestimo + total_juros

print(f"Total de juros a serem pagos: {total_juros}")
print(f"Total a ser pago: {total}")
