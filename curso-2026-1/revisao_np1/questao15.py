PESO_AVALIACAO = 3
PESO_EXAME = 5
PESO_LABORATORIO = 2

avaliacao = float(input("Digite a nota da Avaliação: "))
exame = float(input("Digite a nota do Exame: "))
laboratorio = float(input("Digite a nota do Laboratório: "))

media = (avaliacao*PESO_AVALIACAO + exame*PESO_EXAME + laboratorio*PESO_LABORATORIO) / (PESO_LABORATORIO + PESO_EXAME + PESO_AVALIACAO)
print(f"Media = {media: .2f}")

if (media < 3):
    print("Reprovado!")
elif (media >= 3) and (media < 5):
    print("Recuperacao")
else:
    print("Aprovado")