# entrada de dados da lanchonete
qtdHamburguer = int(input("Quantidade de Hamburguer: "))
qtdRefrigerante = int(input("Quantidade de Refrigerante: "))
qtdBatatas = int(input("Quantidade de porções de batata: "))

# processamento (calculo da conta)
resultadoConta = (18 * qtdHamburguer) + (6 * qtdRefrigerante) + (9 * qtdBatatas)

# saída de dados
print("Total a ser pago = ", resultadoConta)