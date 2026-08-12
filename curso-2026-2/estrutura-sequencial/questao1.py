# entrada de dados
qtd_hambuguer = int(input('Digite a quantidade de hamburguer: '))
qtd_refrigerante = int(input('Digite a quantidade de refrigerante: '))
qtd_batata = int(input('Digite a quantidade de batatas: '))

valor_unitario_hamburguer = 18
valor_unitario_refri = 6
valor_unitario_batata = 9.99

# processamento
preco_total = (qtd_batata*valor_unitario_batata) + (qtd_hambuguer*valor_unitario_hamburguer) + (qtd_refrigerante*valor_unitario_refri)

# saída de dados
print(f'Total a ser pago é: {preco_total}')