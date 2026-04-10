quantidade_acima_100 = 0
media_lucro_animacao = 0
titulo_mais_lucrativo = ''
maior_lucro = 0
contador_animacao = 0

while True:
    titulo = input('Digite o título do filme: ')
    print(f'{titulo.upper()}')
    genero = int(input('Digite o genero[1-Ação, 2-Drama, 3-Comédia, 4-Animação]: '))
    orcamento = float(input('Valor do Orçamento (em milhões): '))
    apuracao = float(input('Valor da apuração (em milhões): '))

    # LOGICA DA APLICACAO ----
    # Apresenta o lucro e o título de cada filme
    lucro = apuracao - orcamento
    print(f'{titulo} possui um lucro de {lucro}')

    # Calculo para saber o maior lucro
    if (lucro > maior_lucro):
        maior_lucro = lucro
        titulo_mais_lucrativo = titulo

    # Calculo da médias dos lucros de animação
    if (genero == 4):
        media_lucro_animacao += lucro
        contador_animacao += 1
    
    # Quantidade de filmes com lucro acima de 100M
    if (lucro > 100):
        quantidade_acima_100 += 1

    opcao = input('Deseja Continuar? [S/N]')
    if (opcao.lower() == 'nao' or opcao.lower() == 'não' or opcao.lower() == 'n'):
        break
    else:
        continue


media_lucro_animacao = media_lucro_animacao/contador_animacao

print(f'*' * 30)
print(f'O filme {titulo_mais_lucrativo} é o mais lucrativo com {maior_lucro}')
print(f'Quantidade de filmes com lucro acima de 100M: {quantidade_acima_100}')
print(f'Média dos lucros dos filmes de animação: {media_lucro_animacao}')
print(f'*' * 30)
