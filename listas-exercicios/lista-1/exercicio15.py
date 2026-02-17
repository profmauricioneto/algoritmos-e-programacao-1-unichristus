# Um banco deseja simular o valor final de um empréstimo com juros simples. Dados de entrada:
# Valor do empréstimo
# Taxa de juros mensal (%)
# Quantidade de meses
# Desenvolva um algoritmo que:
# Leia os dados;
# Calcule o valor final a ser pago;
# Informe o total de juros pagos.

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
