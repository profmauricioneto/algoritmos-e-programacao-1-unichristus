# definir a função calcular
def calcular(num_primeiro, num_segundo, operacao):
    if (operacao.lower() == '+'):
        return num_primeiro + num_segundo
    elif (operacao.lower() == '-'):
        return num_primeiro - num_segundo
    elif (operacao.lower() == '*'):
        return num_primeiro * num_segundo
    elif (operacao.lower() == '/'):
        if (num_segundo == 0):
            print('Erro! Divisor não pode ser zero!')
            return 'error'
        else:
            return num_primeiro / num_segundo
    else:
        print(f'Erro. Operação {operacao} não suportada pela função')
        return 'error'
    
# função principal
def main():
    num_1 = float(input('Digite o primeiro numero: '))
    num_2 = float(input('Digite o segundo numero: '))
    operacao = input('Digite a operação a ser realizada (+,-,*,/): ')
    
    resultado = calcular(num_1, num_2, operacao)
    
    if (resultado != 'error' or type(resultado) == 'number'):
        print(f'O resultado da operação de {operacao} = {resultado}')

# chamada da função   
main()
