qtd_termos = int(input("Digite a quantidade de termos da série harmônica: "))
somatorio = 0

for i in range(1, qtd_termos + 1):
    somatorio = somatorio + 1/i
    
print(f"O valor da série harmônica é: {somatorio}")