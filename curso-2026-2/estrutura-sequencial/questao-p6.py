salario_base = float(input('Salario Base: '))
porcentagem = float(input('Porcentagem de aumento: '))

aumento = salario_base * (porcentagem/100)
salario_novo = salario_base + aumento

print(f'Aumento calculado: {aumento: .2f}')
print(f'Salario novo: {salario_novo: .2f}')