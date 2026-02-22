lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    if (lado_a == lado_b) and (lado_b == lado_c):
        print("O triângulo é equilátero.")
    elif (lado_a == lado_b) or (lado_b == lado_c) or (lado_a == lado_c):
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Estes valores não são compatíveis com um triângulo!") 