salario = float(input("Digite o salario: "))
aumento = float(input("Digite o aumento em porcentagem: "))

aumento = aumento/100
aumento_concedido = aumento*salario
novo_salario = salario + aumento_concedido

print(f"Aumento baseado na porcentagem passada: {aumento_concedido: .2f}")
print(f"Salario total: {novo_salario: .2f}")
