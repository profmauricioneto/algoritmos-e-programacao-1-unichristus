soma_dos_quadrados = 0
quadrado_da_soma = 0
contador = 1

while(contador <= 10):
    soma_dos_quadrados += (contador**2)
    quadrado_da_soma += contador
    contador += 1

quadrado_da_soma = quadrado_da_soma**2
diferenca = quadrado_da_soma - soma_dos_quadrados

print(f'Quadrado da Soma: {quadrado_da_soma}')
print(f'Soma dos Quadrados: {soma_dos_quadrados}')
print(f'Diferença: {diferenca}')