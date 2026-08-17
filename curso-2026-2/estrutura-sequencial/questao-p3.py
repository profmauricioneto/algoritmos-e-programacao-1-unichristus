# entrada de dados
nota1 = float(input("Digite a nota 1: "))
peso1 = float(input('Digite o peso 1: '))
nota2 = float(input('Digite a nota 2: '))
peso2 = float(input('Digite o peso 2: '))

# processamento
media_pond = (nota1*peso1 + nota2*peso2)/(peso1 + peso2)

# saída de dados
print(f'A média é: {media_pond: .2f}')