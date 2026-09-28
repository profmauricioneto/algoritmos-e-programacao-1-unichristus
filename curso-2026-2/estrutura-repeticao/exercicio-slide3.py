fatorial = int(input('Fatorial de: '))
fat = 1

if (fatorial < 0):
    print('Não existe fatorial de negativos!')
else:
    for i in range(1, fatorial+1):
        fat = fat*i
        print(f'Estado atual de fat = {fat}')
print(f'Fatorial de {fatorial} = {fat}')