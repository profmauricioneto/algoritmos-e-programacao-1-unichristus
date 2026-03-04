idade = int(input("Digite sua idade: "))

if (idade % 2 == 0):
    idade = idade + 10
else:
    idade = idade * 2

print(f"Valor de Idade: {idade}")