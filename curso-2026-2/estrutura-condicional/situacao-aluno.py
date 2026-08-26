nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2
print(f'A média = {media: .2f}')

if (media >= 7.0):
    print('Aprovado')
elif (media < 4.0):
    print('Reprovado!')
else:
    print('Final')
    
    nota_final = float(input('Digite a nota final: '))
    media_final = (media + nota_final)/2
    print(f'Media da Final = {media_final: .2f}')
    
    if (media_final >= 5.0):
        print(f'Aprovado na Final')
    else:
        print(f'Reprovado na Final')

print('Fim de Algoritmo.')
# if (media >= 7.0):
#     print('Aprovado! Vaitimbora!')
# else:
#     if(media < 4.0):
#         print('Reprovado! Fica ai!')
#     else:
#         print('Final! Fica mais um pouco!')