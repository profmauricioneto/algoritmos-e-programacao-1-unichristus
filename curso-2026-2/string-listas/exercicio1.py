DNA = "AGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCTAGCTTAGCCAACTGAAGCT"

# peça para o usuario entrar com o padrão procurado e, caso exista esse padrão, diga quantas vezes ele se repete!
# use operador IN e COUNT

padrao = input('Digite o padrão baseado em [t/a/g/c]: ')
possui_padrao = padrao.upper() in DNA

if (possui_padrao):
    print('Padrão encontrado!')
    qtd_padrao = DNA.count(padrao.upper())
    print(f'Quantidade de repetições: {qtd_padrao}')
    # primeira_ocorrencia = DNA.find(padrao.upper())
    # print(f'Primeira ocorrencia do padrão: {primeira_ocorrencia}')
    # continuar a questao: mostrar todas as ocorrencias do padrao encontrado!
    posicao = 0
    contador = 0
    while True:
        posicao = DNA.find(padrao, posicao)
        contador += 1
        print(f'padrão encontrado na posição = {posicao} - contador = {contador}')
        if posicao == -1:
            break 
        
        posicao = posicao + 1

        
else:
    print('Padrão não encontrado.')