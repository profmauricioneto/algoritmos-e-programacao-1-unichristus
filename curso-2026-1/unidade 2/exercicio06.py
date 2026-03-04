peso = float(input("Peso (Kg): "))
altura = float(input("Altura (m):"))

imc = peso/(altura**2)

print(f"IMC = {imc: .2f}")