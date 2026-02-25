# entrada de dados
quantidade_horas = int(input("Quantidade de horas trabalhadas: "))
valor_hora = float(input("Valor da hora: "))

# processamento
salario_bruto = quantidade_horas * valor_hora
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (ir + inss + sindicato)

# saída de dados
print(f"+ Salário Bruto: R${salario_bruto: .2f}")
print(f"- INSS: R${inss: .2f}")
print(f"- IR: R${ir: .2f}")
print(f"- Sindicato: R${sindicato: .2f}")
print(f"= Salário Liquido: R${salario_liquido: .2f}")
