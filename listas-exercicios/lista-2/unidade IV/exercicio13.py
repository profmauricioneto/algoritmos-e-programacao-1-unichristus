ano = int(input("Entre com o ano a ser avaliado: "))

if (ano % 400 == 0 or ano % 4 == 0) and (ano % 100 != 100):
    print("Ano é bissexto.")
else:
    print("Não é ano bissexto.")