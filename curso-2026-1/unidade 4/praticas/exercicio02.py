media = 0
contador = 0

while True:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print('Idade Inválida')
    elif idade == 0:
        break
    else:
        contador += 1
        media += idade

if contador == 0:
    print("Não houve calculo!")
else:
    media = media/contador
    print(f'Quantidade de Idades: {contador}')
    print(f'Media de idades foi: {media: .1f}')
