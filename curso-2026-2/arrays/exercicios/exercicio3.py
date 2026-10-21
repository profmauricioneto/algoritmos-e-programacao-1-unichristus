qtd = 5

nome_produtos = ['']*qtd
qtd_produtos = [0]*qtd
preco_produtos = [0]*qtd

total_vendas = 0

# entrada de dados
for i in range(qtd):
    nome_produtos[i] = input(f'Nome Produto[{i}]: ')
    qtd_produtos[i] = int(input(f'Quantidade[{i}]: '))
    preco_produtos[i] = float(input(f'Preço Unitário[{i}]: '))
    
    total_vendas += (qtd_produtos[i]*preco_produtos[i])

# procurando a maior quantidade de vendas
# maior_valor = preco_produtos[0]
mais_vendido = qtd_produtos[0]
posicao_mais_vendido = 0
for i in range(qtd):
    if (mais_vendido < qtd_produtos[i]):
        mais_vendido = qtd_produtos[i]
        posicao_mais_vendido = i
    # if (maior_valor < preco_produtos[i]):
    #     maior_valor = preco_produtos[i]

# relatório de vendas
print('-'*40)
print('-'*20 + 'RELATORIO DE VENDAS' + '-'*20)
print('-'*40)

for i in range(qtd):
    print('')
    print(f'Produto: {nome_produtos[i]}')
    print(f'Valor Unitário:  {preco_produtos[i]}')
    print(f'Quantidade de vendas do produto: {qtd_produtos[i]}')
    print(f'Valor da venda desses produtos: {(preco_produtos[i]*qtd_produtos[i])}')
    
comissao = 545 + 0.05*total_vendas
print(f'Comissão do Vendedor = R${comissao: .2f}')
print(f'Produto mais vendido = {nome_produtos[posicao_mais_vendido]}')
print(f'Quantidade Vendida = {qtd_produtos[posicao_mais_vendido]}')
