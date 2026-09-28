salario_inicial = float(input('Salário Inicial: '))
ano_atual = int(input('Ano Atual: '))
aumento_porcentagem = 1.5

for ano in range(2005, ano_atual + 1):
    salario_inicial = salario_inicial + salario_inicial*(aumento_porcentagem/100)
    # salario_inicial = salario_inicial*(1 + aumento_porcentagem/100)
    print(f'Ano Referência: {ano} - Salário Atual: {salario_inicial: .2f}')
    aumento_porcentagem = aumento_porcentagem*2