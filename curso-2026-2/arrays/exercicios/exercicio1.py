# ALGORITMO apresentacao_pares

#     DECLARE valores[5]: NUMERICO
#             i: NUMERICO
            
#     PARA i <- 0 ATE 4 FACA:
#         ESCREVA("Digite o valor: ")
#         LEIA(valores[i])
        
#         SE valores[i] % 2 = 0 ENTAO
#             INICIO
#                 ESCREVA("Numero Par")
#                 ESCREVA("Valor: ", valores[i])
#                 ESCREVA("Posicao: ", i)
#             FIM

# FIM_ALGORITMO

valores = [0] * 5

for i in range(len(valores)):
    valores[i] = int(input(f'Digite um valor[{i}]:'))
    
    if (valores[i] % 2 == 0):
        print('Valor Par')
        print(f'Valor = {valores[i]}')
        print(f'Posição = {i}')
        