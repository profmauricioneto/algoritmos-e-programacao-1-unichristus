nota_trabalho = float(input("Nota do Trabalho: "))
nota_avaliacao = float(input("Nota da Avaliação Semestral: "))
nota_exame_final = float(input("Nota do Exame Final: "))

media_final = ((nota_trabalho*2) + (nota_avaliacao*3) + (nota_exame_final*5))/10

if (media_final < 3):
    print("Reprovado!")
elif (media_final >= 3 and media_final < 5):
    print("Recuperação!")
else:
    print("Aprovado!")
