import random

print('Adivinhe o número! Escolha o nível:')
print('1 - Beginner\n2 - Hard\n3 - Insane')
nivel = int(input('Digite o nível desejado: '))

num_aleatorio = random.randint(1, 10)
tentativas = 0

if (nivel == 1):
    while(True):
        chute = int(input('Valor do chute [1 a 10]: '))
        tentativas += 1
        
        if (num_aleatorio == chute):
            print('Acertou!')
            break
        else:
            if (num_aleatorio > chute):
                print('Palpite: chute mais cima')
            else:
                print('Palpite: chute mais baixo')
    print(f'Quantidade de tentivas: {tentativas}')
elif (nivel == 2):
    while(True):
        if (tentativas == 3):
            break
        chute = int(input('Valor do chute [1 a 10]: '))
        tentativas += 1
        if (num_aleatorio == chute):
            print('Acertou!')
            break
        else:
            if (num_aleatorio > chute):
                print('Palpite: chute mais cima')
            else:
                print('Palpite: chute mais baixo')
    print(f'Quantidade de tentivas: {tentativas}')
elif (nivel == 3):
    while(True):
        if (tentativas == 3):
            break
        chute = int(input('Valor do chute [1 a 10]: '))
        tentativas += 1
        if (num_aleatorio == chute):
            print('Acertou!')
            break
    print(f'Quantidade de tentivas: {tentativas}')
else:
    print('Opção Inválida de nivel!')