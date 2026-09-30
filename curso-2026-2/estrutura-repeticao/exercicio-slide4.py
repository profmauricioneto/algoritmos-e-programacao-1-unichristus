# total_pares = 0

# for i in range(10):
#     num = int(input('Numero: '))
#     if (num % 2 == 0):
#         total_pares += num
        
# print(f'Soma dos pares: {total_pares}')

soma_primos = 0
for i in range(5):
    num = int(input('Numero: '))
    flag = True
    for j in range(2, num):
        if (num % j == 0):
            flag = False
    if flag:
        print(f'O valor {num} é primo!')
        soma_primos = soma_primos + num
    else:
        print(f'O valor {num} NAO é primo!')
print(f'Soma dos primos = {soma_primos}')