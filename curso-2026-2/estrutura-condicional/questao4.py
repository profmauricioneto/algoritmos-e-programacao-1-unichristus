genero = input('Digite o gênero [Masculino/Feminino]: ')
altura = float(input('Digite a altura: '))
peso_ideal = 0
genero = genero.upper()

if (genero == 'MASCULINO'):
    peso_ideal = (72.7 * altura) - 58
elif (genero == 'FEMININO'):
    peso_ideal = (62.1 * altura) - 44.7
else:
    print('Genero Inválido')

print(f'Peso ideal = {peso_ideal: .2f}')