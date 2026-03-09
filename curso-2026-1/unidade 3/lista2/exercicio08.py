import math

a = float(input("Valor do fator de a = "))

if (a == 0):
    print("A equacao nao é do segundo grau")
    exit()
else:
    b = float(input("Valor do fator de b = "))
    c = float(input("Valor do fator de c = "))
    delta = (b**2) - (4*a*c)
    print(f"Valor delta = {delta}")
    if (delta < 0):
        print("Nao ha raizes reais")
        exit()
    elif (delta == 0):
        x1 = (-b + math.sqrt(delta))/(2*a)
        print(f"Raiz da equacao = {x1}")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"Raizes da equacao = {x1} e {x2}")
