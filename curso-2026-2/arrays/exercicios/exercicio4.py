# dados iniciais
codigo_produtos = [123, 124, 125, 126, 127]
qtd_produtos = [4, 8, 3, 7, 5]

while(True):
    valor_codigo = int(input('Código do produto: '))
    
    if (valor_codigo == 0):
        print('Fim da Consulta/Venda')
        break
    else:
        # percorrer o array de códigos e verificar se o código existe ou não
        encontrado = False
        for i in range(len(codigo_produtos)):
            if codigo_produtos[i] == valor_codigo:
                encontrado = True         
                # percorrer o array de códigos e verificar se o código existe ou não
                # perguntar qual a quantidade e verificar se quantidade é o suficiente (verificando no array de quantidade)
                # atualizar o array de quantidade caso seja o valor suficiente!
                qtd = int(input('Quantidade requerida: '))
                if (qtd <= qtd_produtos[i]):
                    print('Pedido atendido. Obrigado e volte sempre')
                    qtd_produtos[i] = qtd_produtos[i] - qtd
                else:
                    print('Não temos essa quantidade em estoque!')
                    print(f'Quantidade atual em estoque: {qtd_produtos[i]}')

        if (not encontrado):
            print('Código nexistente na base de dados!')
# ao final apresentar o relatório
print('------------- RELATORIO ---------------')
for i in range(len(codigo_produtos)):
    print(f'Código Produto = {codigo_produtos[i]} - Quantidade = {qtd_produtos[i]}')