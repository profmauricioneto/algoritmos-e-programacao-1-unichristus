cont_faixa_1 = 0
cont_faixa_2 = 0
cont_faixa_3 = 0
cont_faixa_4 = 0
cont_faixa_5 = 0

for quantidade in range(1, 9):
    idade = int(input('Qual a sua idade: '))
    if (idade <= 15):
        cont_faixa_1 += 1
    elif (idade > 15 and idade <= 30):
        cont_faixa_2 += 1
    elif (idade > 30 and idade <= 45):
        cont_faixa_3 += 1
    elif (idade > 45 and idade <= 60):
        cont_faixa_4 += 1
    else:
        cont_faixa_5 += 1

print(f'Quantidade na faixa 1: {cont_faixa_1}')
print(f'Quantidade na faixa 2: {cont_faixa_2}')
print(f'Quantidade na faixa 3: {cont_faixa_3}')
print(f'Quantidade na faixa 4: {cont_faixa_4}')
print(f'Quantidade na faixa 5: {cont_faixa_5}')

print(f'Porcentagem de pessoas na primeira faixa: {(cont_faixa_1/8)*100}')

print(f'Porcentagem de pessoas na ultima faixa: {(cont_faixa_5/8)*100}')