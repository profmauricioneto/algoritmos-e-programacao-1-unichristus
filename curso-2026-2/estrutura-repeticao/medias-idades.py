soma_idades = 0
contador = 0

while(True):
    idade = int(input('Digite a idade[0 para sair]: '))
    
    if (idade == 0):
        break
    elif (idade < 0):
        print('Entrada Inválida!')
    else:
        soma_idades += idade
        contador += 1
if (contador > 0):
    print(f'Media das idades: {soma_idades/contador}')
else:
    print('Nenhuma entrada validada!')