def texto_ajuda():
    print('Esse é o código exemplo de subrotina!')

def calculo(salario):
    percentual = int(input('Percentual: '))
    valor = (salario * percentual)/100
    # salario = 1234
    return valor


texto_ajuda()
salario = float(input('Digite o salario: '))
aumento = calculo(salario)
novo_salario = salario + aumento
print(f'Novo salario é: {novo_salario: .2f}')
print(salario)