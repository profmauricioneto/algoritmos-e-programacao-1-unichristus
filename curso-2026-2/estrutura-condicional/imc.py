peso = float(input('Digite o peso atual (kg): '))
altura = float(input('Digite a altura (m): '))

imc = peso / (altura ** 2)
print(f'IMC calculado é = {imc: .2f}')

# situação baseada no IMC
if(imc >= 25):
    print('Peso em Excesso!')
else:
    print('Saudável!')