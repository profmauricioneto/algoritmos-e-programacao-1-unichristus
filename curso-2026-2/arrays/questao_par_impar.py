valores = [0] * 10

# preencher o vetor com novos valores
for i in range(len(valores)):
    valores[i] = int(input(f'Digite o valor[{i}]: '))
print(valores)

# percorrer o vetor, verificando quem é par e quem é ímpar
cont_par = 0
cont_impar = 0
for i in range(len(valores)):
    if (valores[i] % 2 == 0):
        cont_par += 1
    else:
        cont_impar += 1
        
# saída de informações
print(f'Quantidade de valores Pares: {cont_par}')
print(f'Quantidade de valores Ímpares: {cont_impar}')

# ------------- REFATORACAO ----------------
valores = [0] * 10
cont_par = 0
cont_impar = 0

for i in range(len(valores)):
    valores[i] = int(input(f'Valor[{i}]: '))
    
    if (valores[i] % 2 == 0):
        cont_par += 1
    else:
        cont_impar += 1
        
# saída de informações
print(f'Quantidade de valores Pares: {cont_par}')
print(f'Quantidade de valores Ímpares: {cont_impar}')  
