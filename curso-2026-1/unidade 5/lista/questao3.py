def fatorial(valor):
    fat = 1
    for i in range(1, valor + 1):
        fat = fat * i
    return fat

valor = int(input('Digite um valor inteiro positivo: '))
resultado = fatorial(valor)
print(f'Valor do fatorial de {valor}: {resultado}')