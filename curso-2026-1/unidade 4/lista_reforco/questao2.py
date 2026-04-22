while True:
    numero = int(input('Digite um número inteiro positivo: '))
    if (numero >=1) and (numero <=10):
        for i in range(1, 11):
            print(f'{numero}x{i} = {numero*i}')
        break
    else:
        print('Número Inválido. Digite um valor de 1 a 10!')