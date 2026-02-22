nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
peso_1 = float(input("Digite o peso da primeira e da segunda nota: "))

nota_3 = float(input("Digite a terceira nota: "))
peso_2 = float(input("Digite o peso da terceira nota: "))

media = ((nota_1 + nota_2)*peso_1 + nota_3*peso_2)/(peso_1 + peso_2)
print(f"A média ponderada é = {media: .2f}")

if media >= 6.0:
    print("Aprovado.")
else:
    print("Reprovado.")