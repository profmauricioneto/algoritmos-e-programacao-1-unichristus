num = int(input('Digite um número positivo: '))
while num <= 0:
    print('Número Inválido! Tente novamente!')
    num = int(input('Digite novamente um número positivo.'))
print(f'O número digitado é = {num}')

cont = 0
while cont < 10:
    cont = cont + 1
    print(f'Contador: {cont}')
    if (cont == 5):
        break
print('Fim!')

while True:
    idade = int(input('Digite sua idade: '))
    if (idade > 0):
        break
print(f'Idade Digitada: {idade}')