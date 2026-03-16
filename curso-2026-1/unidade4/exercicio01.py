# Usando a estrutura ENQUANTO, escreva um algoritmo que peça para o usuário entrar com 5 números e ao final mostre a quantos desses números eram pares

# FACA EM PYTHON!

cont_par = 0
contador = 0
while(contador < 5):
    num = int(input("Digite um número: "))
    if (num % 2 == 0):
        # cont_par = cont_par + 1
        cont_par += 1
    contador += 1
print(f"Quantidade de Pares: {cont_par}")