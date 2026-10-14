notas = [0] * 10
print(notas)

nomes = [''] * 10
print(nomes)

for i in range(len(notas)):
    notas[i] = int(input(f'Digite o valor da nota[{i}]: '))
# print(notas)

for i in range(len(notas)):
    print(f'nota[{i}] digitada: {notas[i]}')
    
# for nota in notas:
#     print(nota)
    