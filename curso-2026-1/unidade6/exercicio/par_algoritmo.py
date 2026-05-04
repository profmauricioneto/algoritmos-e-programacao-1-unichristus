numeros = [0]*5

for i in range(0, 5):
    numeros[i] = int(input('Digite um valor inteiro: '))
    if (numeros[i] % 2 == 0):
        print(f'O número {numeros[i]} é par e sua posição é {i}')

print(numeros)