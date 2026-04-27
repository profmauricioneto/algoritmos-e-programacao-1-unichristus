# Um banco oferece uma aplicação de renda fixa com taxa de juros compostos mensalmente. O cliente quer saber em quantos meses o valor aplicado dobrará. O programa parte do valor inicial e multiplica-o pela taxa a cada mês, contando as iterações até o valor atingir ou superar o dobro do capital inicial. Implemente um programa Python que leia o valor inicial (float) e a taxa de juros mensal em percentual (float, ex: 1.5 para 1,5%). O programa deve usar um laço while para simular mês a mês e exibir o número de meses necessários para dobrar o capital. Use apenas variáveis float e int.

valor_inicial = float(input('Digite o valor inicial do montante: '))
taxa_juros = float(input('Digite a taxa de juros: '))

taxa_juros = taxa_juros/100
meses = 0
valor_inicial_referencia = valor_inicial*2
while(valor_inicial <= valor_inicial_referencia):
    meses += 1
    valor_inicial = valor_inicial + (valor_inicial*taxa_juros)
    print(f'Valor no mês {meses} = {valor_inicial}')
    
print(f'Quantidade de meses até dobrar o valor inicial: {meses} meses')