import random

qtd_jogadas = int(input("Digite a quantidade de jogadas: "))

for i in range(1, qtd_jogadas + 1):
    d1 = random.randint(1, 100)
    d2 = random.randint(1, 100)
    if (d1 > d2):
        print(f"O dado d1 ganhou! d1: {d1} e d2: {d2}")
    elif (d1 == d2):
        print(f"Deu empate! d1: {d1} e d2: {d2}")
    else:
        print(f"O dado d2 ganhou! d1: {d1} e d2: {d2}")