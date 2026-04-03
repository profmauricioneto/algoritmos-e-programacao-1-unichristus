num = int(input("Digite um número positivo: "))
if (num <= 0):
    print("Entrada Inválida!")
else:
    # SOLUCAO COM PARA
    serie_harmonica = 0
    for i in range(1, num + 1):
        serie_harmonica += 1/i # serie_harmonica = serie_harmonica + 1/i
    print("RESOLUCAO COM PARA")
    print(f"Valor da Serie Harmonica para {num} valores é: {serie_harmonica}")
    
    # SOLUCAO COM ENQUANTO
    contador = 1
    serie_harmonica_2 = 0
    while(contador <= num):
        serie_harmonica_2 += 1/contador
        contador += 1
    print("RESOLUCAO COM ENQUANTO")
    print(f"Valor da Serie Harmonica para {num} valores é: {serie_harmonica_2}")
    
    # SOLUCAO COM REPITA ATE