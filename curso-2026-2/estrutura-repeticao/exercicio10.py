# versão com somente while (enquanto)
# valor_tabuada = int(input('Montar tabuada de: '))
# comeco = int(input('Começar por: '))
# termino = int(input('Terminar em: '))

# if (comeco > termino):
#     print('Não é possível fazer a tabuada com essas entradas!')
# else:
#     while(comeco <= termino):
#         print(f'{valor_tabuada} * {comeco} = {comeco * valor_tabuada}')
#         comeco = comeco + 1
# print('Fim Tabuada!')

# versão com REPITA 
valor_tabuada = int(input('Montar tabuada de: '))
comeco = int(input('Começar por: '))
termino = int(input('Terminar em: '))

if (comeco > termino):
    print('Não é possível fazer a tabuada com essas entradas!')
else:
    while True:
        print(f'{valor_tabuada} * {comeco} = {comeco * valor_tabuada}')
        comeco = comeco + 1
        if (comeco > termino):
            break
print('Fim Tabuada!')