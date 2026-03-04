lado_a = int(input("Digite o valor do lado A: "))
lado_b = int(input("Digite o valor do lado B: "))
lado_c = int(input("Digite o valor do lado C: "))

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    print("O triângulo ABC é um triangulo válido.")
else:
    print("ABC nao lados de um triangulo")