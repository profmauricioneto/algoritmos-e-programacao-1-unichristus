valores_produtos = [0.0]*10
quantidade_vendidos = [0]*10
total_vendidos = 0
salario = 0

for i in range(0, 10):
    valores_produtos[i] = float(input('Digite o valor unitário do produto: '))
    quantidade_vendidos[i] = int(input('Quantidade de produto vendido: '))
    total_vendidos = total_vendidos + valores_produtos[i]*quantidade_vendidos[i]

salario = 545 + 0.05*total_vendidos

maior_venda = quantidade_vendidos[0]
indice_maior_venda = 0
print('-'*30)
for i in range(0, 10):
    print(f'Valor unitário do produto: {valores_produtos[i]}')
    print(f'Quantidade vendida: {quantidade_vendidos[i]}')
    print(f'Total do produto: {valores_produtos[i]*quantidade_vendidos[i]}')
    if (maior_venda < quantidade_vendidos[i]):
        maior_venda = quantidade_vendidos[i]
        indice_maior_venda = i
print(f'Total das Vendas: {total_vendidos}')
print(f'Comissão do Vendedor: {salario}')
print(f'Maior quantidade de vendas: {maior_venda} no indice: {indice_maior_venda}')
print('-'*30)
