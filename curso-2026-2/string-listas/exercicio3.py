frase1 = input('Digite o texto: ').upper()
frase2 = input('Digite o texto a buscar: ').upper()

posicao = frase1.find(frase2)

if (posicao == -1):
    print(f'{frase2} não encontrada')
else:
    print(f'{frase2} encontrada - posição = {posicao}')