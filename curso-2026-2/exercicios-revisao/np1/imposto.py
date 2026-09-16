valor_produto = float(input('Digite o valor do produto: '))
estado = input('Digite o estado de destino [MG/SP/RJ/MS]: ').lower()

taxa_mg = 0.07
taxa_sp = 0.12
taxa_rj = 0.15
taxa_ms = 0.08
preco_final = 0
valor_imposto = 0
if (estado == 'mg'):
    valor_imposto = valor_produto*taxa_mg
    preco_final = valor_produto + valor_imposto
elif (estado == 'sp'):
    valor_imposto = valor_produto*taxa_sp
    preco_final = valor_produto + valor_imposto
elif (estado == 'rj'):
    valor_imposto = valor_produto*taxa_rj
    preco_final = valor_produto + valor_imposto
elif (estado == 'ms'):
    valor_imposto = valor_produto*taxa_ms
    preco_final = valor_produto + valor_imposto
else:
    print('Estado Inválido. Não foi possível calcular o imposto!')

print(f'Preço Final: {preco_final: .2f}')
print(f'Valor do Imposto: {valor_imposto: .2f}')
