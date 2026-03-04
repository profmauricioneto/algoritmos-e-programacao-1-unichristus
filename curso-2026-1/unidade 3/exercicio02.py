trabalho = float(input("Nota do Trabalho: "))
peso_trabalho = int(input("Peso do Trabalho: "))

avaliacao = float(input("Nota do Avaliacao: "))
peso_avaliacao = int(input("Peso do Avaliacao: "))

exame_final = float(input("Nota do Exame Final: "))
peso_exame_final = int(input("Peso do Exame Final: "))

# processamento
media_pond = ((trabalho*peso_trabalho) + (avaliacao * peso_avaliacao) + (exame_final * peso_exame_final)) / (peso_avaliacao + peso_trabalho + peso_exame_final)

print(f"Media = {media_pond: .2f}")

if (media_pond >= 8):
    print("Conceito A")
elif (media_pond < 8) and (media_pond >= 7):
     print("Conceito B")
elif (media_pond < 7) and (media_pond >= 6):
    print("Conceito C")
elif (media_pond < 6) and (media_pond >= 5):
    print("Conceito D")
else:
    print("Conceito E")
    

# if (media_pond >= 8):
#     print("Conceito A")
# else:
#     if (media_pond <= 4):
#         print("Conceito E")
#     else:
#         if