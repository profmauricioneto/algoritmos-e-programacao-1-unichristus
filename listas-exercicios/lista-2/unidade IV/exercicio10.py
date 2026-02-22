salario_atual = float(input("Digite o salário atual do funcionário: "))
tempo_ano = int(input("Digite a quantidade anos que o funcionario trabalhou na empresa: "))
salario_reajustado = 0

if (salario_atual <= 500 and tempo_ano < 1):
    salario_reajustado = salario_atual + 0.25*salario_atual
elif (salario_atual > 500 and salario_atual <= 1000) and (tempo_ano >= 1 and tempo_ano <= 3):
    salario_reajustado = salario_atual + 0.2*salario_atual + 100
elif (salario_atual > 1000 and salario_atual <= 1500) and (tempo_ano >= 4 and tempo_ano <= 6):
    salario_reajustado = salario_atual + 0.15*salario_atual + 200
elif (salario_atual > 1500 and salario_atual <= 2000) and (tempo_ano >= 7 and tempo_ano <= 10):
    salario_reajustado = salario_atual + 0.1*salario_atual + 300
else:
    salario_reajustado = salario_atual + 500
    
print(f"Salário reajustado: {salario_reajustado: .2f}")