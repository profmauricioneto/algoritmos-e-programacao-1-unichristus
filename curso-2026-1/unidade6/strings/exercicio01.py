texto = input('Digite o texto de entrada: ')
padrao_busca = input('Digite o padrão de busca desejada: ')

resultado = texto.lower().find(padrao_busca.lower())
if (resultado == -1):
    print(f'Padrão {padrao_busca} não encontrado!')
else:
    print(f'Padrão encontrado no indice: {resultado}!')