# ALGORITMO verificador_primos

#     DECLARE valores[9]: NUMERICO
#             i, j: NUMERICO
#             cont_divisores: NUMERICO
            
#     PARA i <- 0 ATE 8 FACA:
#         ESCREVA("Digite um valor inteiro: ")
#         LEIA(valores[i])
#         cont_divisores = 0
#         PARA j <- 1 ATE valores[i] FACA:
#             SE (valores[i] % j = 0) ENTAO
#                 cont_divisores = cont_divisores + 1
#         SE cont_divisores = 2 ENTAO
#             ESCREVA("Numero Primo")
#             ESCREVA("Numero: ", valores[i])
#             ESCREVA("Posicao: ", i)
# FIM_ALGORITMO

valores = [0] * 9

for i in range(len(valores)):
    valores[i] = int(input(f'Digite o {i} valor: '))
    
    cont_divisores = 0
    for j in range(1, valores[i] + 1):
        if (valores[i] % j == 0):
            cont_divisores += 1
    if (cont_divisores == 2):
        print('Número Primo')
        print(f'Valor = {valores[i]}')
        print(f'Posição = {i}')