import math

a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

if a == 0:
    print('Não é equação do segundo grau!')
else:
    delta = b**2 - 4*a*c
    print(f'Delta = {delta: .2f}')
    
    if (delta < 0):
        print('Não há raizes reais!')
    elif (delta == 0):
        x1 = (-b + math.sqrt(delta))/(2*a)
        print(f"Raiz 1 = {x1: .2f}")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f'Raiz 1 = {x1: .2f}')
        print(f'Raiz 2 = {x2: .2f}')