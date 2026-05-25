quantidade = 3
codigos_produtos = [0]*quantidade
quantidade_produtos = [0]*quantidade
# preenchendo a base dados
for i in range(0, quantidade):
    codigos_produtos[i] = int(input('Digite o código do produto: '))
    quantidade_produtos[i] = int(input('Digite a quantidade deste produto: '))

# logica do sistema
while True:
    codigo_cliente = int(input('Digite o código do cliente: '))
    # condição para saída do sistema
    if (codigo_cliente == 0):
        break
    codigo_produto = int(input('Digite o código do produto: '))
    quantidade_produto = int(input('Quantidade do Produto: '))
    # condição para verificar se existe o produto na base de dados
    existe_produto = False
    indice_produto = -1
    for i in range(0, quantidade):
        if (codigos_produtos[i] == codigo_produto):
            existe_produto = True
            indice_produto = i
            print(f'indice_produto = {indice_produto}')
    # verificar o estado de existe_produto e indice_produto
    if (existe_produto):
        if (quantidade_produtos[indice_produto] < quantidade_produto):
            print('Desculpe! Não temos estoque suficiente para atender a demanda!')
        else:
            print('Pedido Atendido! Volte sempre!')
            quantidade_produtos[indice_produto] = quantidade_produtos[indice_produto] - quantidade_produto
            
# mostrando base de dados atualizada após a venda!
for i in range(0, quantidade):
    print(f'código produto: {codigos_produtos[i]}')
    print(f'Quantidade: {quantidade_produtos[i]}')
    
print('Saindo do programa!')
    
    