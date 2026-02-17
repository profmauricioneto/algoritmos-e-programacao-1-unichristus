sexo = input("Digite o sexo do usuário: ")
sexo = sexo.lower()
altura = float(input("Digite a altura do usuário: "))
peso_ideal = 0

if sexo == "homem":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Error: Não foi possível fazer o cálculo.")
    
print(f"Valor do peso ideal: {peso_ideal: .2f}")