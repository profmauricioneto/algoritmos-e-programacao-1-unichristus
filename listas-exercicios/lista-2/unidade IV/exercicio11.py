peso = float(input("Peso do Usuário: "))
altura = float(input("Altura do Usuário: "))

imc = peso/(altura ** 2)

if (imc <= 18.5):
    print("Abaixo do Peso.")
elif (imc > 18.6 and imc <= 24.9):
    print("Saudável.")
elif (imc > 25 and imc < 29.9):
    print("Peso em Excesso.")
elif (imc > 30 and imc < 34.9):
    print("Obesidade Grau 1.")
elif (imc > 35 and imc < 39.9):
    print("Obesidade Grau 2 (severa)")
else: 
    print("Obesidade Grau 3 (mórbida)")