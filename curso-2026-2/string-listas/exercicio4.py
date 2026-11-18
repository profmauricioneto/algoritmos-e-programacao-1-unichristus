texto = input('Digite o texto: ').lower()
repetido = ''

for l in texto:
    if l not in repetido:
        print(f'{l}: {texto.count(l)}x')
        repetido = repetido + l