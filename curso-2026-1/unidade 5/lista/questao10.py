def calcular_salario_liquido(salario_bruto):
    desconto_inss = salario_bruto * 0.08 
    print(f'Desconto de R$:{desconto_inss} do INSS')
    salario_liquido = salario_bruto - desconto_inss
    return salario_liquido

def main():
    salario_bruto = float(input('Digite o salário bruto: '))
    salario_liquido = calcular_salario_liquido(salario_bruto)
    print(f'Salario Liquido R$:{salario_liquido: .2f}')
    
    print(len('mauricio'))

if __name__ == '__main__':
    main()