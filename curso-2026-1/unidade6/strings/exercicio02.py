palavra = input('Digite uma palavra: ').upper()
palavra = list(palavra)
print(palavra)
contagem = []

# contagem da quantidade de repetições
for i in range(0, len(palavra)):
    cont = 0
    for j in range(0, len(palavra)):
        if (palavra[i] == palavra[j]):
            cont += 1
    contagem.append(cont)
print(contagem)

# apresentando os elementos com suas quantidades
for i in range(0, len(palavra)):
    eh_repetido = False
    for j in range(i):
        if (palavra[i] == palavra[j]):
            eh_repetido = True
            break
    if (not eh_repetido):
        print(f'{palavra[i]}: {contagem[i]}x')