import math

cateto_a = float(input("Valor do cateto A: "))
cateto_b = float(input("Valor do cateto B: "))

hipotenusa = math.sqrt(((cateto_a ** 2) + (cateto_b ** 2)))

print(f"O valor da hipotenusa deste triângulo é: {hipotenusa}")