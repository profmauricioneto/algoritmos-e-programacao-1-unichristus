inicio = int(input('Digite o valor de inicio: '))
fim = int(input('Digite o valor do final: '))

for i in range(inicio, fim + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if (primo):
        print(f'{i} é primo')