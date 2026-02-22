genero = input("Digite o seu genero (F/M): ")
genero = genero.lower()

if genero == "f":
    print("Feminino")
elif genero == "m":
    print("Masculino")
else:
    print("Sexo Inválido")