valores = [0]*10

cont_par = 0
cont_impar = 0
for i in range(0, 10):
    valores[i] = int(input('Digite um valor inteiro: '))
    if (valores[i] % 2 == 0):
        cont_par = cont_par + 1
        print(f'O valor {valores[i]} é par!')
    else:
        cont_impar = cont_impar + 1
        print(f'O valor {valores[i]} é ímpar')
        
print(f'Quantidade de Pares: {cont_par}')
print(f'Quantidade de Impares: {cont_impar}')
    