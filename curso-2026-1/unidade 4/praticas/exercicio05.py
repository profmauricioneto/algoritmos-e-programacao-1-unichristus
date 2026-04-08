valor = int(input('Digite um valor inteiro acima de  1: '))
if (valor <= 1):
    print('Entrada Inválida!')
else:
    contador = 0
    for i in range(1, valor + 1):
        if (valor % i == 0):
            contador += 1
    if (contador == 2):
        print(f'Numero {valor} é cousin!')
    else:
        print(f'Numero {valor} NÃO é cousin!')