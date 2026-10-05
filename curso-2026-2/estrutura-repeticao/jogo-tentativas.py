import random

contador = 0
num_aleatorio = random.randint(1, 10)

while(True):
    chute = int(input('Valor do chute [1 a 10]: '))
    contador += 1
    
    if (num_aleatorio == chute):
        print('Acertou!')
        break
    else:
        if (num_aleatorio > chute):
            print('Palpite: chute mais cima')
        else:
            print('Palpite: chute mais baixo')
print(f'Quantidade de tentivas: {contador}')    