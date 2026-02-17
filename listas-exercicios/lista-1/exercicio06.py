valor_hora = float(input("Qual o valor da hora de trabalho: "))
horas_trabalhadas = int(input("Quantas horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas;
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - inss - ir - sindicato

message = f"""
    + Salario bruto: R$: {salario_bruto}
    - IR (11%): R$ {ir}
    - INSS (8%): R$ {inss}
    - sindicato (5%): R$ {sindicato}
    = Salário liquido: R$ {salario_liquido}
"""

print(message)