nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2
print(f'A média = {media: .2f}')

# if (media >= 7.0):
#     print('Aprovado')
# elif (media < 4.0):
#     print('Reprovado!')
# else:
#     print('Final')

if (media >= 7.0):
    print('Aprovado! Vaitimbora!')
else:
    if(media < 4.0):
        print('Reprovado! Fica ai!')
    else:
        print('Final! Fica mais um pouco!')