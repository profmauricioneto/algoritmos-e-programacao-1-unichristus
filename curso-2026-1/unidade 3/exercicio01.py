# QUESTAO DA SITUACAO DE UM ALUNO (APROVADO, REPROVADO OU FINAL)

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2)/2
print(f"Media = {media: .2f}")

# if aninhado!
if (media >= 7):
    print("Aprovado! Vaitimbora!")
else:
    if(media  < 4):
        print("Reprovado! Fica ai vai!")
    else:
        print("Final! Fica mais um pouco...")
        
        nota_final = float(input("Nota Final: "))
        media_final = (media + nota_final)/2
        print(f"Media Final = {media_final: .2f}")
        # resultado da final
        if (media_final >= 5):
            print("Aprvado na Final! Sortudo!")
        else:
            print("Reprovado na Final! Coitado..fica pra proxima.")
        
        
# usando elif
# if (media >= 7):
#     print("Aprovado!")
# elif (media < 4):
#     print("Reprovado")
# else:
#     print("Final")

