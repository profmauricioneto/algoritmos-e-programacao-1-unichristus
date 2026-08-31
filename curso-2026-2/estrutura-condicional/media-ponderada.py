nota_lab = float(input('Nota do Trabalho em Laboratório: '))
nota_avaliacao = float(input('Nota da Avaliação Semestral: '))
nota_exame_final = float(input('Nota do Exame Final: '))

peso_lab = 2
peso_avaliacao = 3
peso_exame_final = 5

media_pond = (nota_lab*peso_lab + nota_avaliacao*peso_avaliacao + nota_exame_final*peso_exame_final)/(peso_lab + peso_avaliacao + peso_exame_final)
print(f'A média ponderada é: {media_pond: .2f}')

if (media_pond >= 8.0):
    print('Conceito A')
elif (media_pond >= 7.0 and media_pond < 8.0):
    print('Conceito B')
elif (media_pond >= 6.0 and media_pond < 7.0):
    print('Conceito C')
elif (media_pond >= 5.0 and media_pond < 6.0):
    print('Conceito D')
else:   
    print('Conceito E')