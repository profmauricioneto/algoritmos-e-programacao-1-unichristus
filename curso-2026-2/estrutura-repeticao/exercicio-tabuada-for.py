numero_tabuada = int(input('Qual o valor da tabuada: '))
inicio = int(input("Inicio em: "))
termino = int(input("Termina em: "))

for i in range(inicio, termino + 1):
    print(f'{numero_tabuada} x {i} = {numero_tabuada * i}')