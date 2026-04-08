while True:
    titulo = input('Digite o título do filme: ')
    print(f'{titulo.upper()}')
    genero = int(input('Digite o genero[1-Ação, 2-Drama, 3-Comédia, 4-Animação]: '))
    orcamento = float(input('Valor do Orçamento (em milhões): '))
    apuracao = float(input('Valor da apuração (em milhões): '))

    # LOGICA DA APLICACAO ----

    opcao = input('Deseja Continuar? [S/N]')
    if (opcao.lower() == 'nao' or opcao.lower() == 'não' or opcao.lower() == 'n'):
        break
    else:
        continue

