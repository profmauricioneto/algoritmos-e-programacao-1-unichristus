# Usando a estrutura ENQUANTO, peça para o usuário entrar com um número inteiro maior que zero e calcule o fatorial desse número

# FACA EM PYTHON
num = int(input("Digite um valor inteiro: "))
if num < 0:
    print("Não é possível calcular o valor de fatorial negativo!")
else:
    fat = 1
    contador = 1
    while(contador <= num):
        fat = fat*contador
        contador += 1
    print(f"Fatorial = {fat}")